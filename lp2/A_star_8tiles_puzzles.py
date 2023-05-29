from queue import PriorityQueue
import numpy as np

# Define the goal state
goal_state = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 0]])

# Define the possible moves
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # (right, left, down, up)

# Helper function to get the coordinates of the empty tile
def get_empty_tile(board):
    return np.argwhere(board == 0)[0]

# Helper function to generate the neighboring states
def generate_neighbors(board, empty_tile):
    neighbors = []
    for move in moves:
        new_pos = empty_tile + move
        if np.all(new_pos >= 0) and np.all(new_pos < 3):
            neighbor = board.copy()
            neighbor[empty_tile[0], empty_tile[1]] = board[new_pos[0], new_pos[1]]
            neighbor[new_pos[0], new_pos[1]] = 0
            neighbors.append(neighbor)
    return neighbors

# Helper function to calculate the Manhattan distance heuristic
def calculate_heuristic(board):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = board[i, j]
            if value != 0:
                target_row = (value - 1) // 3
                target_col = (value - 1) % 3
                distance += abs(i - target_row) + abs(j - target_col)
    return distance

# A* algorithm for solving the 8-puzzle
def solve_8_puzzle(initial_state):
    queue = PriorityQueue()
    queue.put((0, initial_state))
    visited = set()

    while not queue.empty():
        _, current_state = queue.get()

        if np.array_equal(current_state, goal_state):
            return current_state

        empty_tile = get_empty_tile(current_state)
        neighbors = generate_neighbors(current_state, empty_tile)

        for neighbor in neighbors:
            hashable_neighbor = tuple(map(tuple, neighbor))
            if hashable_neighbor not in visited:
                priority = calculate_heuristic(neighbor)
                queue.put((priority, neighbor))
                visited.add(hashable_neighbor)

    return None

# Example usage:
initial_state = np.array([[1, 2, 3],
                          [4, 5, 6],
                          [0, 7, 8]])

solution = solve_8_puzzle(initial_state)
if solution is not None:
    print("Solution found:")
    print(solution)
else:
    print("No solution found.")