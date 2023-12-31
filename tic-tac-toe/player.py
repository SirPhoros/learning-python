import math
import random
from enum import Enum


class Letter(Enum):
    X = "X"
    O = "O"


class Player:
    def __init__(self, letter):
        """
        Initialize a player with a letter (X or O).
        """
        self.letter = letter

    def get_move(self, game):
        """
        Get the player's move based on the current game state.
        """
        pass


class RandomComputerPlayer(Player):
    def get_move(self, game):
        """
        Get a random valid move for the computer player.
        """
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def get_move(self, game):
        """
        Get the human player's move through user input.
        """
        valid_square = False
        val = None
        while not valid_square:
            square = input(f"{self.letter}'s turn. Input move (0-8): ")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError("Invalid move. Please choose an available square.")
                valid_square = True
            except ValueError:
                print("Invalid input. Please enter a valid number (0-8).")
        return val


class SuperComputerPlayer(Player):
    def get_move(self, game):
        """
        Get the computer player's move using a minimax algorithm.
        """
        if len(game.available_moves()) == 0:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)["position"]
        return square

    def minimax(self, state, player):
        max_player = self.letter
        other_player = "O" if player == "X" else "X"

        # state and not game, as in every iteration of the game we are going to pass a "state" of the game, like a screenshot to be analysed.

        # Base Case
        if state.current_winner == other_player:
            # return position AND score as it is needed to keep track for minimax to work

            empty_squares = state.num_empty_squares()
            if other_player == max_player:
                score = 1 * (empty_squares + 1)
            else:
                score = -1 * (empty_squares + 1)
            return {"position": None, "score": score}

        # no empty squares
        elif not state.empty_squares():
            return {"position": None, "score": 0}

        if player == max_player:
            best = {"position": None, "score": -math.inf}  # each score should maximise
        else:
            best = {"position": None, "score": math.inf}  # score should minimise

        for possible_move in state.available_moves():
            # step 1: make a move, try that spo
            state.make_move(possible_move, player)

            # step 2: recurse using minimax to simulate a game after that move
            # alternate players
            sim_score = self.minimax(state, other_player)

            # step 3: undo the move
            state.board[possible_move] = " "
            state.current_winner = None
            sim_score["position"] = possible_move

            # step 4: update the dictionary if necessary
            if player == max_player:
                if sim_score["score"] > best["score"]:
                    best = sim_score  # replace best

            else:
                if sim_score["score"] < best["score"]:
                    best = sim_score  # replace best

        return best
