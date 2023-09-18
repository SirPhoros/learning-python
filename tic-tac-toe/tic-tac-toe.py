from player import HumanPlayer, RandomComputerPlayer, SuperComputerPlayer, Letter
import time


class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]  # The will represent the 3x3 grid
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i * 3 : (i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_nums():
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

    def make_move(self, square, letter):
        # if valid move, the assign the square to a letter
        # then return true. If invalid, return false
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter

            return True
        return False

    def winner(self, square, letter):
        # winner if 3 in a row, collumn or diagonal
        ## Row
        row_ind = square // 3
        row = self.board[row_ind * 3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        ## Column
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        ## Diagonal
        ## ONLY IF THE SQAURE IS AN EVEN NUMBER, AS THESE ARE THE ONLY POSSIBLE TO WIN A DIAGONAL
        # (0, 2, 4, 6, 8)
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True

        # if all of these conditions fail:
        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    current_letter = Letter.X  # Use the Letter enum to represent the starting letter

    while game.empty_squares():
        if current_letter == Letter.O:  # Use the Letter enum for player comparison
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, current_letter.value):
            if print_game:
                print(current_letter.value + f" makes a move to square {square}")
                game.print_board()
                print("")
                if game.current_winner:
                    break

            current_letter = (
                Letter.O if current_letter == Letter.X else Letter.X
            )  # Use the Letter enum

            time.sleep(0.8)

    if print_game:
        if game.current_winner:
            print(f"{game.current_winner} wins")
        else:
            print("It's a tie")


if __name__ == "__main__":
    x_player = HumanPlayer(Letter.X)
    o_player = SuperComputerPlayer(Letter.O)
    game = TicTacToe()
    play(game, x_player, o_player, print_game=True)
