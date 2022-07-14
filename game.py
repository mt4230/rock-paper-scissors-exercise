import random
print("--------------------------------------")
print("WELCOME TO ROCK PAPER SCISSORS GAME")
print("--------------------------------------")
# USER INPUTS
user_choice = input ("Please make a selection ('rock', 'paper', 'scissors'):")
user_choice = user_choice.lower()

# You chose: 'rock'
print (f"You chose:'{user_choice}'")

# VALIDATE USER INPUTS
valid_options = ["rock","paper","scissors"]

#breakpoint()
if user_choice not in valid_options:
    print("OOPS INVALID ENTRY TRY AGAIN")
    exit() # quit()

# COMPUTER CHOICE
# import random in starting of program - Good approach
computer_choice = random.choice(valid_options)
print (f"Computer chose:'{computer_choice}'")

# DETERMINE THE WINNER

# Adapted from code shared in slack by Bonnie Auger at 08:38 pm on July 13, 2022
# https://nyu-tech-2335.slack.com/archives/C5WPFSB52/p1657672686150239
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("Rock crushes scissors. You win!")
    else:
        print("Paper covers rock. You lose.")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Paper covers rock. You win!")
    else:
        print("Scissors cuts paper. You lose.")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("Scissors cuts paper. You win!")
    else:
        print("Rock crushes scissors. You lose.")

print("--------------------------------------")
print("Thanks for playing. Please play again!")
















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