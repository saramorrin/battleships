import random

def welcome_message():
    """
    Print statements used in the welcome message,
    will display each time a new game begins.
    """
    print("Welcome to Battleships")
    print("You have 5 pirate ships to sink")
    player_name = input("Please enter your name Captain: ")


class GameBoard:
    """
    Create computer gameboard using letters for x row 
    and numbers for y row.
    """
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
    """
    Create 5 ships on computer gameboard in randomly 
    generated locations. These ships will be hidden 
    from the player.
    """
    def __init__(self, board):
        self.board = board

    def create_ships(self):
        for i in range(4):
            self.x_row, self.y_column = random.randint(0, 3), random.randint(0, 3)
            while self.board[self.x_row][self.y_column] == "x":
                self.x_row, self.y_column = random.randint(0, 3), random.randint(0, 3)
            self.board[self.x_row][self.y_column] = "x"
        return self.board

    def get_user_input(self):
        """
        Requests player input of co-ordinates to guess location of a
        computers ship. Allows for while loop to run to ensure that the 
        data inputted is valid, error message will display to user if 
        data is not valid. Loop will repeatedly request data until it 
        is valid.
        """
    try:
        x_row = input("Enter the row of the ship between 1-4: ")
        while x_row not in '1234':
            print('Uh oh, you must enter a value between 1-4')
            x_row = input("Enter the row of the ship between 1-4: ")

        y_column = input("Enter the column letter of the ship between A-D: ").upper()
        while y_column not in "ABCD":
            print('Uh oh, you must enter a letter between A-D')
            y_column = input("Enter the column letter of the ship between A-D: ").upper()
            return int(x_row) - 1, GameBoard.get_letters_to_numbers()[y_column]
        #except ValueError and KeyError:
            #print("Uh oh, that was not a valid input")
            return self.get_user_input()


    #def count_hit_ships(self):
        """
        Counts number of hit ships in the game.
        """
        #hit_ships = 0
        #for row in self.board:
        #    for column in row:
        #        if column == "x":
        #           hit_ships += 1
    #return hit_ships


    def RunGame(): 
        computer_board = GameBoard([[" "] * 4 for i in range(4)])
        user_guess_board = GameBoard([[" "] * 4 for i in range(4)])
        Battleship.create_ships(computer_board)
        #start 10 turns
        turns = 10
        while turns > 0:
            GameBoard.print_board(user_guess_board)
            #get user input
            user_x_row, user_y_column = Battleship.get_user_input(object)
            #check if duplicate guess
            while user_guess_board.board[user_x_row][user_y_column] == "o" or user_guess_board.board[user_x_row][user_y_column] == "x":
                print("You guessed that one already")
                user_x_row, user_y_column = Battleship.get_user_input(object)
            #check for hit or miss
            if computer_board.board[user_x_row][user_y_column] == "x":
                print("Excellent shot Captain, you sunk 1 ship!\n")
                user_guess_board.board[user_x_row][user_y_column] = "x"
            else:
                print("It's a miss, try again Captain!\n")
                user_guess_board.board[user_x_row][user_y_column] = "o"
            #check for win or lose
            if Battleship.count_hit_ships(user_guess_board) == 5:
                print("You hit all 5 ships!")
                break
            else:
                turns -= 1
                print(f"You have {turns} turns remaining\n")
                if turns == 0:
                    print("Sorry you ran out of turns, better luck next time!\n")
                    GameBoard.print_board(user_guess_board)
                    break

                if __name__ == '__main__':
                    RunGame()


def new_game():

    welcome_message()
  

new_game()