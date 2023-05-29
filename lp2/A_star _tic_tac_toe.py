import math


class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.winning_combinations = [
            [(0, 0), (0, 1), (0, 2)],  # Row 1
            [(1, 0), (1, 1), (1, 2)],  # Row 2
            [(2, 0), (2, 1), (2, 2)],  # Row 3
            [(0, 0), (1, 0), (2, 0)],  # Column 1
            [(0, 1), (1, 1), (2, 1)],  # Column 2
            [(0, 2), (1, 2), (2, 2)],  # Column 3
            [(0, 0), (1, 1), (2, 2)],  # Diagonal 1
            [(0, 2), (1, 1), (2, 0)]   # Diagonal 2
        ]

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def get_winner(self):
        for combination in self.winning_combinations:
            symbols = [self.board[row][col] for row, col in combination]
            if symbols == ['X', 'X', 'X']:
                return 'X'
            elif symbols == ['O', 'O', 'O']:
                return 'O'
        return None

    def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def get_valid_moves(self):
        valid_moves = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    valid_moves.append((row, col))
        return valid_moves

    def evaluate_board(self):
        winner = self.get_winner()
        if winner == 'X':
            return 1
        elif winner == 'O':
            return -1
        else:
            return 0

    def minimax(self, depth, alpha, beta, maximizing_player):
        if depth == 0 or self.get_winner() is not None or self.is_board_full():
            return self.evaluate_board()

        if maximizing_player:
            max_eval = -math.inf
            for move in self.get_valid_moves():
                row, col = move
                self.board[row][col] = 'X'
                eval_score = self.minimax(depth - 1, alpha, beta, False)
                self.board[row][col] = ' '
                max_eval = max(max_eval, eval_score)
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = math.inf
            for move in self.get_valid_moves():
                row, col = move
                self.board[row][col] = 'O'
                eval_score = self.minimax(depth - 1, alpha, beta, True)
                self.board[row][col] = ' '
                min_eval = min(min_eval, eval_score)
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break
            return min_eval

    def get_best_move(self):
        best_eval = -math.inf
        best_move = None
        for move in self.get_valid_moves():
            row, col = move
            self.board[row][col] = 'X'
            eval_score = self.minimax(4, -math.inf, math.inf, False)
            self.board[row][col] = ' '
            if eval_score > best_eval:
                best_eval = eval_score
                best_move = move
        return best_move


def main():
    game = TicTacToe()

    while True:
        game.print_board()

        if game.current_player == 'X':
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))
            if not game.make_move(row, col):
                print("Invalid move! Try again.")
                continue
        else:
            print("AI is making a move...")
            best_move = game.get_best_move()
            game.make_move(best_move[0], best_move[1])

        winner = game.get_winner()
        if winner:
            game.print_board()
            print(f"{winner} wins!")
            break

        if game.is_board_full():
            game.print_board()
            print("It's a tie!")
            break


if __name__ == '__main__':
    main()
