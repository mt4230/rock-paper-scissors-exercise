
import random

print("WELCOME TO ROCK PAPER SCISSORS GAME")


# USER INPUTS


user_choice = input ("Please make a selection ('rock', 'paper', 'scissors'):")


# You chose: 'rock'
print (f"You chose:'{user_choice}'")


# VALIDATE USER INPUTS


# COMPUTER CHOICE



valid_options = ["rock","paper","scissors"]
computer_choice = random.choice(valid_options)
print (f"Computer chose:'{computer_choice}'")

# DETERMINE THE WINNER


# DISPLAY RESULTS

# -------------------
# Welcome 'Player One' to my Rock-Paper-Scissors game...
# -------------------
# Please choose either 'rock', 'paper', or 'scissors': rock
# You chose: 'rock'
# The computer chose: 'paper'
# -------------------
# Oh, the computer won. It's ok.
# -------------------
# Thanks for playing. Please play again!