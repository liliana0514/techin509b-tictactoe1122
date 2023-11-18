# tests.py
import pytest
from logic import Player, Game

@pytest.fixture
def game():
    player1 = Player("Player1", "X")
    player2 = Player("Player2", "O")
    return Game(player1, player2)

def test_initial_board(game):
    assert all(all(cell == ' ' for cell in row) for row in game.board)

def test_switch_player(game):
    initial_player = game.current_player
    game.switch_player()
    assert game.current_player != initial_player

def test_make_move(game):
    row, col = 1, 1
    game.make_move(row, col)
    assert game.board[row][col] == game.current_player.symbol

def test_invalid_move(game):
    row, col = 1, 1
    game.make_move(row, col)
    assert not game.is_valid_move(row, col)

def test_valid_move(game):
    row, col = 1, 1
    assert game.is_valid_move(row, col)

def test_winner_horizontal(game):
    for i in range(3):
        game.make_move(i, 0)
    assert game.check_winner()
    assert game.get_winner() == game.current_player

def test_winner_vertical(game):
    for i in range(3):
        game.make_move(0, i)
    assert game.check_winner()
    assert game.get_winner() == game.current_player

def test_winner_diagonal(game):
    for i in range(3):
        game.make_move(i, i)
    assert game.check_winner()
    assert game.get_winner() == game.current_player

def test_winner_reverse_diagonal(game):
    for i in range(3):
        game.make_move(i, 2 - i)
    assert game.check_winner()
    assert game.get_winner() == game.current_player

def test_draw_game(game):
    for i in range(3):
        for j in range(3):
            game.make_move(i, j)
    assert not game.check_winner()
    assert game.is_board_full()

def test_player_assignments(game):
    assert game.players[0].symbol != game.players[1].symbol

