# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.
import random

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self):
        if self.name == 'Bot':
            row = random.randint(0, 2)
            col = random.randint(0, 2)
        else:
            row = int(input(f"{self.name}, enter row (0-2): "))
            col = int(input(f"{self.name}, enter col (0-2): "))
        return row, col

class Game:
    def __init__(self, player1, player2):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.players = [player1, player2]
        self.current_player = None
        self.winner = None

    def print_board(self):
        for row in self.board:
            print("|".join(row))
        print()

    def start_game(self):
        self.current_player = self.players[0]
        while True:
            self.print_board()
            row, col = self.current_player.make_move()
            if self.is_valid_move(row, col):
                self.make_move(row, col)
            else:
                print("Invalid move. Try again.")
                continue

            if self.check_winner() or self.is_board_full():
                self.print_board()
                break
            self.switch_player()

    def make_move(self, row, col):
        self.board[row][col] = self.current_player.symbol

    def switch_player(self):
        self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                self.winner = self.current_player
                return True

            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                self.winner = self.current_player
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            self.winner = self.current_player
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            self.winner = self.current_player
            return True

        return False

    def is_board_full(self):
        return all(all(cell != ' ' for cell in row) for row in self.board)

    def is_valid_move(self, row, col):
        return 0 <= row <= 2 and 0 <= col <= 2 and self.board[row][col] == ' '

    def get_winner(self):
        return self.winner
