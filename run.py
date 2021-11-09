import random

def welcome_message():
    """
    Print statements used in the welcome message,
    will display each time a new game begins
    """
  
    print("Welcome to Battleships")
    print("You have 5 pirate ships to sink")
    player_name = input("Please enter your name Captain: ")


class GameBoard:
    def __init__(self, board):
        self.board = board

    def get_letters_to_numbers():
        letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3 }
        return letters_to_numbers

    def print_board(self):
      print("  A B C D ")
      print(" *-*-*-*-*")
      row_number = 1
      for row in self.board:
          print("%d|%s|" % (row_number, "|".join(row)))
          row_number += 1


class Battleship:
    def __init__(self, board):
        self.board = board

    def create_ships(self):
        for i in range(4):
            self.x_row, self.y_column = random.randint(0, 3), random.randint(0, 3)
            while self.board[self.x_row][self.y_column] == "x":
                self.x_row, self.y_column = random.randint(0, 3), random.randint(0, 3)
            self.board[self.x_row][self.y_column] = "x"
        return self.board


def new_game():

    welcome_message()
  

new_game()