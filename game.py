import pygame
import sys
import board
import solver
import time

# Constants
WINDOW_WIDTH = board.WINDOW_WIDTH
WINDOW_HEIGHT = board.WINDOW_HEIGHT + 100  # Extra space for buttons
FPS = 60

# Colors
WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Sliding Puzzle")
clock = pygame.time.Clock()

def main():
    running = True
    solving = False
    solution_path = []
    solution_index = 0

    while running:
        mouse_pos = pygame.mouse.get_pos()
        redraw_hover = board.redraw_button.collidepoint(mouse_pos)
        solve_hover = board.solve_button.collidepoint(mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and not solving:
                if event.key == pygame.K_LEFT:
                    board.move_tile("LEFT")
                elif event.key == pygame.K_RIGHT:
                    board.move_tile("RIGHT")
                elif event.key == pygame.K_UP:
                    board.move_tile("UP")
                elif event.key == pygame.K_DOWN:
                    board.move_tile("DOWN")
                elif event.key == pygame.K_r:
                    board.create_board()
            elif event.type == pygame.MOUSEBUTTONDOWN and not solving:
                if redraw_hover:
                    board.create_board()
                elif solve_hover:
                    print("Solving the board...")
                    solution_path = solver.bfs_solver(board.board)
                    if solution_path:
                        print(f"Solution found: {solution_path}")
                        solution_index = 0
                        solving = True
                    else:
                        print("No solution found.")

        if solving and solution_index < len(solution_path):
            board.move_tile(solution_path[solution_index])
            solution_index += 1
            time.sleep(0.3)  # Pause for visibility of each step
        elif solving and solution_index >= len(solution_path):
            solving = False

        screen.fill(WHITE)
        board.draw_board(screen)
        board.draw_buttons(screen, redraw_hover, solve_hover)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
