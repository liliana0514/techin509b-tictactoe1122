# tests/test_tic_tac_toe.py
import pytest
from logic import Player, Game
from cli import *

def test_empty_board():
    game = Game(Player("Player1", "X"), Player("Player2", "O"))
    assert game.get_board() == [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def test_player_assignment():
    player1 = Player("Player1", "X")
    player2 = Player("Player2", "O")
    assert player1.symbol == "X"
    assert player2.symbol == "O"

def test_switch_player():
    game = Game(Player("Player1", "X"), Player("Player2", "O"))
    assert game.current_player == game.players[0]
    game.switch_player()
    assert game.current_player == game.players[1]
    game.switch_player()
    assert game.current_player == game.players[0]

def test_valid_move():
    game = Game(Player("Player1", "X"), Player("Player2", "O"))
    assert game.is_valid_move(1, 1)
    assert not game.is_valid_move(3, 1)
    assert not game.is_valid_move(1, 3)

