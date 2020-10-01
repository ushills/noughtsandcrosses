import random


class XOXGame:
    def __init__(self):
        # initialise the board and available squares
        # 1 | 2 | 3
        # 4 | 5 | 6
        # 7 | 8 | 9
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.player_squares = {"X": [], "O": []}
        self.current_player = None


    def player_turn(self, player, square):
        # need to check square is available first
        if square in self.board:
            self.player_squares[player].append(square)
            self.board.remove(square)
            return self.player_squares
        else:
            return False

    def check_winner(self):
        winning_squares = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
            [1, 5, 9],
            [7, 5, 3],
        ]
        # Check player X
        for w in winning_squares:
            if set(w) <= set(self.player_squares["X"]):
                return "X wins"
            elif set(w) <= set(self.player_squares["O"]):
                return "O wins"
        if len(self.board) == 0:
            return "Draw"
        return False

    def next_player(self):
        if self.current_player is None:
            self.current_player = random.choice(["X", "O"])
        elif self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"
        return self.current_player
