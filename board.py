import pygame
import random
import math

# Constants
TILE_SIZE = 100
BOARD_SIZE = 3
BUTTON_WIDTH = 150
BUTTON_HEIGHT = 50
BUTTON_MARGIN = 20

WINDOW_WIDTH = TILE_SIZE * BOARD_SIZE + 2 * BUTTON_MARGIN
WINDOW_HEIGHT = TILE_SIZE * BOARD_SIZE + 3 * BUTTON_MARGIN + BUTTON_HEIGHT

# Colors
BUTTON_COLOR = (70, 130, 180)
BUTTON_HOVER_COLOR = (100, 149, 237)
BUTTON_TEXT_COLOR = (255, 255, 255)
TILE_COLORS = [
    (255, 102, 102), (255, 178, 102), (255, 255, 102),
    (178, 255, 102), (102, 255, 102), (102, 255, 178),
    (102, 255, 255), (102, 178, 255), (102, 102, 255)
]
TILE_TEXT_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (240, 248, 255)

# Rectangles for buttons
redraw_button = pygame.Rect((WINDOW_WIDTH - 2 * BUTTON_WIDTH - BUTTON_MARGIN) // 2, WINDOW_HEIGHT - BUTTON_HEIGHT - BUTTON_MARGIN, BUTTON_WIDTH, BUTTON_HEIGHT)
solve_button = pygame.Rect((WINDOW_WIDTH + BUTTON_MARGIN) // 2, WINDOW_HEIGHT - BUTTON_HEIGHT - BUTTON_MARGIN, BUTTON_WIDTH, BUTTON_HEIGHT)

pygame.font.init()
font = pygame.font.Font(None, 40)  # Use default font

# Board state
board = []

def create_board():
    global board
    board = list(range(BOARD_SIZE * BOARD_SIZE))
    random.shuffle(board)
    while not is_solvable(board) or board == list(range(BOARD_SIZE * BOARD_SIZE)):
        random.shuffle(board)
    print(f"New board: {board}")

def is_solvable(board):
    inv_count = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] > board[j] != 0:
                inv_count += 1
    return inv_count % 2 == 0

def get_tile_index(tile):
    return board.index(tile)

def move_tile(direction):
    n = BOARD_SIZE
    z = get_tile_index(0)
    if direction == "LEFT" and z % n > 0:
        board[z], board[z - 1] = board[z - 1], board[z]
    elif direction == "RIGHT" and z % n < n - 1:
        board[z], board[z + 1] = board[z + 1], board[z]
    elif direction == "UP" and z >= n:
        board[z], board[z - n] = board[z - n], board[z]
    elif direction == "DOWN" and z < n * (n - 1):
        board[z], board[z + n] = board[z + n], board[z]
    print(f"Moved {direction}: {board}")

def draw_board(screen):
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            tile = board[i * BOARD_SIZE + j]
            if tile != 0:
                rect = pygame.Rect(j * TILE_SIZE + BUTTON_MARGIN, i * TILE_SIZE + BUTTON_MARGIN, TILE_SIZE, TILE_SIZE)
                color = TILE_COLORS[tile % len(TILE_COLORS)]
                pygame.draw.rect(screen, color, rect, border_radius=10)
                pygame.draw.rect(screen, (0, 0, 0), rect, 2, border_radius=10)  # Border
                text_surf = font.render(str(tile), True, TILE_TEXT_COLOR)
                text_rect = text_surf.get_rect(center=rect.center)
                screen.blit(text_surf, text_rect)

def draw_buttons(screen, redraw_hover, solve_hover):
    draw_button(screen, redraw_button, "Redraw", redraw_hover)
    draw_button(screen, solve_button, "Solve", solve_hover)

def draw_button(screen, rect, text, hover):
    color = BUTTON_HOVER_COLOR if hover else BUTTON_COLOR
    pygame.draw.rect(screen, color, rect, border_radius=10)
    pygame.draw.rect(screen, (0, 0, 0), rect, 2, border_radius=10)
    text_surf = font.render(text, True, BUTTON_TEXT_COLOR)
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)

# Initialize the board when the module is imported
create_board()
