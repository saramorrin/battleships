import random

# Global variables here
player_name = None
number_of_ships = 4
game_running = True
welcome_message_str = f"""
Welcome to Battleships
You have {number_of_ships} pirate ships to sink

Instructions:
1) A hit is denoted as "X"
2) A miss is denoted as "O"
3) Your ship locations are denoted with an "S"
"""

def welcome_message():
    """
    Print statements used in the welcome message,
    will display each time a new game begins.
    """
    print(welcome_message_str)
    while True:
        player_name = input("\033[1;32;40mPlease enter your name Captain: ")
        if player_name.isalpha():
            break
        print("Oi Matey! Captain's name only, enter characters A-Z \n")

    print(f"Ahoy! Captain {player_name} \033[0;0m \n")
    

class GameBoard:
    """
    Create computer gameboard using letters 
    for x row and numbers for y row.
    """
    def __init__(self):
        pass

    def get_letters_to_numbers(self, letter):
        """Method to change the letters to number,
        for column reference"""
        letters_to_numbers = {
            "A": 0,
            "B": 1,
            "C": 2,
            "D": 3,
        }
        return letters_to_numbers[letter]

    def print_board(self, board):
        print(" |A|B|C|D|")
        print("----------")
        row_number = 1
        for row in board:
          print("%d|%s|" % (row_number, "|".join(row)))
          print("----------")
          row_number += 1
          


class Battleship:
    """
    Create 4 ships on computer gameboard in randomly 
    generated locations. These ships will be hidden 
    from the player.
    """
    def __init__(self) -> None:
        self.player_board = None
        self.visible_computer_board = None
        self.hidden_computer_board = None
        self.player_score = 0
        self.computer_score = 0

    def create_ships(self):
        """
        Create random ships on a board,
        both player and computer
        """
        # Set Player board
        for i in range(number_of_ships):
            while True:
                row = random.randint(0, 3)
                column = random.randint(0, 3)
                # Ship == S (the letter)
                if self.player_board[row][column] == "S":
                    continue
                self.player_board[row][column] = "S"
                break

        # Set hidden computer board
        for i in range(number_of_ships):
            while True:
                row = random.randint(0, 3)
                column = random.randint(0, 3)
                # Ship == S (the letter)
                if self.hidden_computer_board[row][column] == "S":
                    continue
                self.hidden_computer_board[row][column] = "S"
                break


    def get_user_input(self):
        """
        Requests player input of co-ordinates to guess location of a
        computers ship. Allows for while loop to run to ensure that the 
        data inputted is valid, error message will display to user if 
        data is not valid. Loop will repeatedly request data until it 
        is valid.
        """
        # Ask to guess column
        column = input("Enter the column letter of the ship between A-D: ").upper()
        while column not in ["A", "B", "C", "D"]:
            print("Uh oh, you must enter a letter between A-D\n")
            column = input("Enter the column letter of the ship between A-D: ").upper()

        print("")

        # Ask to guess row
        row = input("Enter the row of the ship between 1-4: ")
        while row not in ["1", "2", "3", "4"]:
            print("Uh oh, you must enter a value between 1-4\n")
            row = input("Enter the row of the ship between 1-4: ")

        return row, column

    def run_game(self):
        """Method for running the game"""
        self.player_board = [[" "] * 4 for i in range(4)]
        self.visible_computer_board = [[" "] * 4 for i in range(4)]
        self.hidden_computer_board = [[" "] * 4 for i in range(4)]
        self.create_ships()
        gb = GameBoard()
        # start 10 turns
        # A hit is == X
        # A miss is an == O
        turns = 1
        while turns < 11:
            print("Your board")
            gb.print_board(self.player_board)

            print("")
            print("Computer board")
            gb.print_board(self.visible_computer_board)

            print(f"Current turn: {turns}")

            # get user input
            while True:
                player_row_guess, player_col_guess = self.get_user_input()
                player_row_guess = int(player_row_guess) - 1
                player_col_guess = gb.get_letters_to_numbers(
                    player_col_guess
                )
                if self.visible_computer_board[player_row_guess][player_col_guess] in ["X", "O"]:
                    print("Shiver me timbers, you have already guessed this position!\n")
                    continue
                break
            print("")

            print("TURN EVENT:")
            # Check if a hit / miss
            if self.hidden_computer_board[player_row_guess][player_col_guess] == "S":
                print(" Excellent shot Captain, you sunk 1 ship!")
                self.hidden_computer_board[player_row_guess][player_col_guess] = "X"
                self.visible_computer_board[player_row_guess][player_col_guess] = "X"
                self.player_score += 1
            else:
                print("It's a miss, try again Captain!")
                self.hidden_computer_board[player_row_guess][player_col_guess] = "O"
                self.visible_computer_board[player_row_guess][player_col_guess] = "O"

            # Computer guess
            while True:
                computer_row_guess = random.randint(0, 3)
                computer_col_guess = random.randint(0, 3)
                if self.hidden_computer_board[computer_row_guess][computer_col_guess] in ["X", "O"]:
                    continue
                break
            print("")
            
            # Check if a hit / miss
            if self.player_board[computer_row_guess][computer_row_guess] == "S":
                print("Batten down the hatches, the computer sunk one of your ships!")
                self.player_board[computer_row_guess][computer_row_guess] = "X"
                self.computer_score += 1
            else:
                print("The computer missed!")
                self.player_board[computer_row_guess][computer_row_guess] = "O"


            if (
                self.computer_score == number_of_ships and
                self.player_score == number_of_ships
            ):
                print("Yo ho ho, It is a draw!")
                return None

            if self.player_score == number_of_ships:
                print("Blow me down! You won Captain!")
                return None

            if self.computer_score == number_of_ships:
                print("Aaaarrrrgggghhhh! The computer won!\n")
                return None

            turns += 1
            print("")

        print("Captain you have run out of turns, it's a draw!\n")

def play_again():
    """
    Asks player if they wish to play again or quit
    """
    print("Would you like to play again?")
    while True: 
        answer = input("Enter Y or N: \n").upper()
        print("")
    
        if answer == "Y":
            new_game()
        elif answer =="N":
            global game_running
            game_running = False
            print("")
            print("Thanks for playing me matey!")
            break
        #else:
            #print("")
            #print("Please enter Y or N")
            #answer = input("Enter Y or N: \n").upper()

            
def new_game():
    #Welcome message to the user
    welcome_message()
    while game_running:
        #Initialise the battleship game
        bs = Battleship()
        bs.run_game()

         #Would you like to play again
        #confirm = input()
        #if confirm == "N":
            #print("Thanks for playing me matey")
            #break

        play_again()

#Entry point to the game
new_game()