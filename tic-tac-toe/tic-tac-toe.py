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

    def available_moves(self):
        moves = []
        for i, spot in enumerate(self.board):
            if spot == " ":
                moves.append(i)
        return moves

    def empty_squares(self):
        return " " in self.board

    def num_empty_squares(self):
        return self.board.count(" ")


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

        letter = "X"  # starting letter

        # iterate while the game still has empty squares in the board
        while game.empty_squares():
            # get the move from the appropriate player
            if letter == "0":
                square = o_player.get_move(game)
            else:
                square = x_player.get_move(game)
