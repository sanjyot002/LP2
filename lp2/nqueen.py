def solve_n_queens(N, board=[], col=0):
    if col == N:
        return board

    for row in range(N):
        if all(row != board[i] and
               row + col != board[i] + i and
               row - col != board[i] - i
               for i in range(col)):
            solution = solve_n_queens(N, board + [row], col + 1)
            if solution is not None:
                return solution

    return None

# Test the code with N = 4
N = 4
solution = solve_n_queens(N)
if solution is None:
    print("No solution exists.")
else:
    for row in solution:
        print(" ".join('Q' if i == row else '.' for i in range(N)))
