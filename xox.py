import random


class XOXGame:
    def __init__(self):
        # initialise the board and available squares
        # 1 | 2 | 3
        # 4 | 5 | 6
        # 7 | 8 | 9
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.player_squares = {"X": [], "Y": []}

    def game(self):
        pass

    def player_turn(self, player, square):
        # need to check square is available first
        if square in self.board:
            self.player_squares[player].append(square)
            self.board.remove(square)
            return self.player_squares
        else:
            return "Invalid Move"

    def check_winner(self):
        winning_squares = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [7, 5, 3]]
        # Check player X
        for w in winning_squares:
            if set(w) <= set(self.player_squares["X"]):
                return "X wins"
            if set(w) <= set(self.player_squares["Y"]):
                return "Y wins"
            elif len(self.board) == 0:
                return "Draw"

    def first_player(self):
        return random.choice(["X", "Y"])
