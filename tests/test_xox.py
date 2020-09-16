import xox as xox


def test_XOXGame_init():
    game = xox.XOXGame()
    assert game.board == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert game.player_squares == {"X": [], "Y": []}


def test_XOXGame_player_turn():
    game = xox.XOXGame()
    assert game.player_turn("X", 1) == {"X": [1], "Y": []}
    assert game.player_turn("Y", 3) == {"X": [1], "Y": [3]}
    assert game.player_turn("X", 2) == {"X": [1, 2], "Y": [3]}
    assert game.player_turn("Y", 2) != {"X": [1, 2], "Y": [3, 2]}


def test_XOXGame_player_turn_invalid_move():
    game = xox.XOXGame()
    assert game.player_turn("X", 1) == {"X": [1], "Y": []}
    assert game.player_turn("Y", 1) == "Invalid Move"
    assert game.player_squares == {"X": [1], "Y": []}


def test_XOXGame_check_winner():
    game = xox.XOXGame()
    game.player_squares = {"X": [1, 2, 3], "Y": []}
    assert game.check_winner() == "X wins"
    game.player_squares = {"X": [], "Y": [4, 5, 6]}
    assert game.check_winner() == "Y wins"
    game.player_squares = {"X": [7, 8, 9], "Y": []}
    assert game.check_winner() == "X wins"
    game.player_squares = {"X": [], "Y": [1, 5, 9]}
    assert game.check_winner() == "Y wins"
    game.player_squares = {"X": [3, 5, 7], "Y": []}
    assert game.check_winner() == "X wins"
    game.player_squares = {"X": [3, 5, 7], "Y": [2, 9, 1]}
    assert game.check_winner() == "X wins"
    game.player_squares = {"X": [4, 7, 8], "Y": [9, 1, 5]}
    assert game.check_winner() == "Y wins"


def test_XOXGame_check_draw():
    game = xox.XOXGame()
    game.board = []
    assert game.check_winner() == "Draw"


def test_first_player():
    game = xox.XOXGame()
    assert game.first_player() in ["X", "Y"]
