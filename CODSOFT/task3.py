# ROCK , PAPER AND SCISSOR GAME

import random  # Imported random module to generate random  choice.

# Function to display choices
def choose():
    print("Choose your move :")
    print("Rock")
    print("Scissor")
    print("Paper\n")

# Initialized user score to 0 
user_score = 0
# List to store score of user
user_scores = []

# Initialized computer score to 0
computer_score = 0
# List to store score of computer
computer_scores = []

# function that displays the logic of game
def game(computer,move):
    # access global scope variable 
    global user_score  
    global computer_score
    # Displaying user choice
    print(f"Your Choice : {move}")
    # Displaying computer's choice
    print(f"Computer's Choice : {computer}")
    # To check if game is tie
    if(computer == move):
        print("Game tie.")
    # To check if user wins and increment their score
    elif((computer == "rock" and move == "paper") or (computer == "paper" and move == "scissor") or (computer == "scissor" and move == "rock")):
        print("You win!")
        user_score += 1
    # Otherwise computer wins
    else:
        print("Computer win!")
        computer_score += 1

# List of choices
choices = ["rock","paper","scissor"]
print("Let's play the game ..")


# Infinite loop to continuously play game
while True:
    try:
        choose()   # Display availabale choices
        move = input("Enter your move from above given choices : ").lower() # Prompt to user enter their move
        if move in choices :        #   To check if user choice is valid
            print("Waiting....")
            computer = random.choice(choices)       # using random module to ransomly select
            game(computer,move)         # Uisng game function
            user_scores.append(user_score)        
            print(f"Your score : {user_score}")       # Printing score of each round of user
            computer_scores.append(computer_score)        
            print(f"Computer's score : {computer_score} \n")       # Printing score of each round of computer
            # Inner loop to ask if user wants to paly again
            while True:
                try:
                    # Prompt to ask if user wants to paly again
                    play_again = input("Do you want to play again ? (yes/no/exit): ").lower()
                    if play_again == 'no' or play_again == 'exit':
                        print(f"Your Final score : {user_score}") # To print final score of user
                        print(f"Computer's Final score : {computer_score}") # To print final score of computer
                        print("Thanks for playing!")
                        exit()      # Exit game
                    elif play_again == 'yes':
                        break
                    else:
                        # raise error if something else is entered rather than yes,no,exit.
                        raise ValueError("Invalid input. Please enter yes or no.") 
                except ValueError as e:
                    print(f"{e}\n")

        else:
            print("Invalid Choice. Please choose from rock, paper and scissor only.\n") # Invalid choice message
    except ValueError as e:
        print("Invalid choice..\n") # Handling input invalid choice
    