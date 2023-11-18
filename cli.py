# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.


from logic import Player, Game

import random

if __name__ == "__main__":
    game_mode = input("Enter game mode (1 for single player, 2 for two players): ")

    if game_mode == '1':
        player1_name = input("Enter name for Player 1: ")
        player1_symbol = input("Enter symbol for Player 1 (X or O): ")
        player1 = Player(player1_name, player1_symbol)

        player2 = Player("Bot", 'O' if player1_symbol.upper() == 'X' else 'X')

    elif game_mode == '2':
        player1_name = input("Enter name for Player 1: ")
        player1_symbol = input("Enter symbol for Player 1 (X or O): ")
        player1 = Player(player1_name, player1_symbol)

        player2_name = input("Enter name for Player 2: ")
        # Automatically assign the opposite symbol to Player 2
        player2_symbol = 'X' if player1_symbol.upper() == 'O' else 'O'
        player2 = Player(player2_name, player2_symbol)

    else:
        print("Invalid game mode. Exiting.")
        exit()

    game = Game(player1, player2)
    game.start_game()
