import xox as xox


def test_XOXGame_init():
    game = xox.XOXGame()
    assert game.board == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert game.player_squares == {"X": [], "O": []}


def test_XOXGame_player_turn():
    game = xox.XOXGame()
    assert game.player_turn("X", 1) == {"X": [1], "O": []}
    assert game.player_turn("O", 3) == {"X": [1], "O": [3]}
    assert game.player_turn("X", 2) == {"X": [1, 2], "O": [3]}
    assert game.player_turn("O", 2) != {"X": [1, 2], "O": [3, 2]}


def test_XOXGame_player_turn_invalid_move():
    game = xox.XOXGame()
    assert game.player_turn("X", 1) == {"X": [1], "O": []}
    assert game.player_turn("O", 1) is False
    assert game.player_squares == {"X": [1], "O": []}


def test_XOXGame_check_winner_rows():
    game = xox.XOXGame()
    game.player_squares = {"X": [1, 2, 3], "O": []}
    assert game.check_winner() == "X wins"
    game.player_squares = {"X": [], "O": [4, 5, 6]}
    assert game.check_winner() == "O wins"
    game.player_squares = {"X": [7, 8, 9], "O": []}
    assert game.check_winner() == "X wins"


def test_XOXGame_check_winner_columns():
    game = xox.XOXGame()
    game.player_squares = {"X": [1, 4, 7], "O": []}
    assert game.check_winner() == "X wins"
    game.player_squares = {"X": [], "O": [2, 5, 8]}
    assert game.check_winner() == "O wins"
    game.player_squares = {"X": [3, 6, 9], "O": []}
    assert game.check_winner() == "X wins"


def test_XOXGame_check_winner_diagonals():
    game = xox.XOXGame()
    game.player_squares = {"X": [], "O": [1, 5, 9]}
    assert game.check_winner() == "O wins"
    game.player_squares = {"X": [3, 5, 7], "O": []}
    assert game.check_winner() == "X wins"


def test_XOXGame_check_draw():
    game = xox.XOXGame()
    game.board = []
    assert game.check_winner() == "Draw"


def test_next_player_no_current_player():
    game = xox.XOXGame()
    assert game.next_player() in ["X", "O"]


def test_next_player():
    game = xox.XOXGame()
    game.current_player = "X"
    assert game.next_player() == "O"
    assert game.next_player() == "X"


def test_XOXGame_real_game():
    game = xox.XOXGame()
    assert game.player_turn("O", 2) == {"X": [], "O": [2]}
    assert game.player_turn("X", 3) == {"X": [3], "O": [2]}
    assert game.player_turn("O", 9) == {"X": [3], "O": [2, 9]}
    assert game.player_turn("X", 7) == {"X": [3, 7], "O": [2, 9]}
    assert game.player_turn("O", 6) == {"X": [3, 7], "O": [2, 9, 6]}
    assert game.player_turn("X", 4) == {"X": [3, 7, 4], "O": [2, 9, 6]}
    assert game.player_turn("O", 1) == {"X": [3, 7, 4], "O": [2, 9, 6, 1]}
    assert game.player_turn("X", 8) == {"X": [3, 7, 4, 8], "O": [2, 9, 6, 1]}
    assert game.player_turn("O", 5) == {"X": [3, 7, 4, 8], "O": [2, 9, 6, 1, 5]}
    assert len(game.board) == 0
    assert game.check_winner() == "O wins"
