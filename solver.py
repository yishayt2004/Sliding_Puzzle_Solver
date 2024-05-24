from collections import deque
from board import BOARD_SIZE

def bfs_solver(board):
    def serialize(board):
        return tuple(board)

    def deserialize(serialized):
        return list(serialized)

    def get_neighbors(state):
        neighbors = []
        n = BOARD_SIZE
        z = state.index(0)
        for direction, delta in zip(["LEFT", "RIGHT", "UP", "DOWN"], [-1, 1, -n, n]):
            nz = z + delta
            if direction == "LEFT" and z % n == 0 or direction == "RIGHT" and z % n == n - 1:
                continue
            if 0 <= nz < len(state):
                new_state = list(state)
                new_state[z], new_state[nz] = new_state[nz], new_state[z]
                neighbors.append((new_state, direction))
        return neighbors

    start_state = serialize(board)
    target_state = serialize(list(range(BOARD_SIZE * BOARD_SIZE)))
    queue = deque([(start_state, [])])
    visited = set()
    visited.add(start_state)

    # cus we are using a deque, we can use popleft() to get the first element
    while queue:
        current_state, path = queue.popleft()
        if current_state == target_state:
            return path

        for neighbor, move in get_neighbors(current_state):
            serialized_neighbor = serialize(neighbor)
            if serialized_neighbor not in visited:
                visited.add(serialized_neighbor)
                queue.append((serialized_neighbor, path + [move]))

    return []

# Example usage
if __name__ == "__main__":
    board = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    print(bfs_solver(board))
