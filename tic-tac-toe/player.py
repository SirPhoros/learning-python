import math
import random


class Player:
    def __init__(self, letter):
        # letter is X or O as in Tic-Tac-Toe
        self.letter = letter

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # get a random valid spot for our next move
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "'s turn. Input move (0-8): ")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again.")
        return val


class SuperComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # randomly choose one, as there is no minimax algorithm to choose.
        if len(game.available_moves()) == 0:
            square = random.choice(game.available_moves())
        # get the square based off the minimax algorithm
        else:
            square = self.minimax(game, self.letter)
        return square

    def minimax(self, state, player):
        max_player = self.letter
        other_player = "O" if player == "X" else "X"

        # state and not game, as in every iteration of the game we are going to pass a "state" of the game, like a screenshot to be analysed.

        # Base Case
        if state.current_winner == other_player:
            # return position AND score as it is needed to keep track for minimax to work

            return {
                "position": None,
                "score": 1 * (state.num_empty_square() + 1)
                if other_player == max_player
                else -1 * (state.num_empty_square() + 1),
            }
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
