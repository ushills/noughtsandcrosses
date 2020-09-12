import xox


def test_XOXGame_init():
    game = xox.XOXGame()
    assert game.board == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert game.player_squares == {"X": [], "Y": []}
