import random

def welcome_message():
    """
    Print statements used in the welcome message,
    will display each time a new game begins
    """
  
    print("Welcome to Battleships")
    print("You have 5 pirate ships to sink")
    player_name = input("Please enter your name Captain: ")


def new_game():

    welcome_message()
  

new_game()