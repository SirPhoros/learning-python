class TicTacToe:
    def __ini__(self):
        self.board = [" " for _ in range(9)]  # The will represent the 3x3 grid
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i * 3 : (i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_numbs():
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")
