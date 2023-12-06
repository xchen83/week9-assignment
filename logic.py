import random
import csv
import os

class Game:
    def __init__(self):
        self.rows = 3
        self.cols = 3
        self.leaveLoop = False
        self.turn = 'X'
        self.turnCounter = 0
        self.board = self.make_empty_board()
        self.log_file_path = 'logs/game_logs_lab10.csv'
        self.loc_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.available_moves = list(range(1, 10))

        if not os.path.exists('logs'):
            os.makedirs('logs')

        if not os.path.exists(self.log_file_path):
            with open(self.log_file_path, 'w', newline='') as log_file:
                writer = csv.writer(log_file)
                writer.writerow(['Winner', 'Player1', 'Player2', 'Moves'])

    def make_empty_board(self):
        return [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]

    def print_board(self):
        for x in range(self.rows):
            print("\n-|---|---|---|-")
            print(" |", end="")
            for y in range(self.cols):
                print("", self.board[x][y], end=" |")
        print("\n-|---|---|---|-")

    def get_winner(self):
        for x in range(3):
            if self.board[x][0] == self.board[x][1] == self.board[x][2]:
                return self.board[x][0]
            elif self.board[0][x] == self.board[1][x] == self.board[2][x]:
                return self.board[0][x]
            elif self.board[0][0] == self.board[1][1] == self.board[2][2]:
                return self.board[0][0]
            elif self.board[0][2] == self.board[1][1] == self.board[2][0]:
                return self.board[0][2]
        return "N"

    def other_player(self):
        if self.turn == 'X':
            self.turn = 'O'
        elif self.turn == 'O':
            self.turn = 'X'

    def modify_array(self, num):
        if num in self.loc_list:
            self.loc_list.remove(num)
            num -= 1
            if num == 0:
                self.board[0][0] = self.turn
            elif num == 1:
                self.board[0][1] = self.turn
            elif num == 2:
                self.board[0][2] = self.turn
            elif num == 3:
                self.board[1][0] = self.turn
            elif num == 4:
                self.board[1][1] = self.turn
            elif num == 5:
                self.board[1][2] = self.turn
            elif num == 6:
                self.board[2][0] = self.turn
            elif num == 7:
                self.board[2][1] = self.turn
            elif num == 8:
                self.board[2][2] = self.turn

    def is_valid_move(self, num):
        num -= 1
        return isinstance(self.board[num // 3][num % 3], int)

    def is_draw(self):
        return self.turnCounter == 9 and self.get_winner() == "N"

    def log_game(self, winner, player1, player2, moves):
        with open(self.log_file_path, 'a', newline='') as log_file:
            writer = csv.writer(log_file)
            writer.writerow([winner, player1, player2, moves])


class Human(Game):
    def __init__(self):
        super().__init__()

    def make_move(self):
        valid_move = False
        while not valid_move:
            try:
                move = int(input("Enter your move (1-9): "))
                if move in self.available_moves and self.is_valid_move(move):
                    valid_move = True
                else:
                    print("Invalid move or move already taken. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        return move


class Bot(Game):
    def __init__(self):
        super().__init__()

    def make_move(self):
        move = random.choice(self.available_moves)
        return move
