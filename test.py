# tests.py

from logic import Player, Game
import pytest

def test_game_initialized_with_empty_board():
    game = Game(Player("Player1", "X"), Player("Player2", "O"))
    assert all(all(cell == ' ' for cell in row) for row in game.board)

def test_players_assigned_unique_pieces():
    player1 = Player("Player1", "X")
    player2 = Player("Player2", "O")
    assert player1.symbol != player2.symbol

def test_switch_player():
    player1 = Player("Player1", "X")
    player2 = Player("Player2", "O")
    game = Game(player1, player2)
    game.switch_player()
    assert game.current_player == player2

def test_valid_move():
    player = Player("Player1", "X")
    game = Game(player, Player("Player2", "O"))
    assert game.is_valid_move(0, 0)

def test_invalid_move():
    player = Player("Player1", "X")
    game = Game(player, Player("Player2", "O"))
    game.make_move(0, 0)
    assert not game.is_valid_move(0, 0)

# Add more tests for other features as needed
