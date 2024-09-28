# Exercise 9: Simple Guessing Game

# Objective: Learn to use loops and conditional statements
# to create a basic game.

# Exercise: Write a program that generates a random number
# between 1 and 10 and asks the user to guess the number. 
# The program should provide feedback and continue to prompt 
# the user until the correct number is guessed.


import random
import re

# Generate the random number in the range [1, 10]
randomNumber = random.randrange(1, 11)
pattern = r'^([1-9]|10)$'

print('The number you select must fall within the range of 1 to 10 inclusively.')

while True:
    userInput = input("Good luck! Guess the number: ")

    # Check if the input is a valid number in the range
    if not re.match(pattern, userInput):
        print("Invalid input. Please enter a number between 1 and 10.")
        continue

    # Convert the input to an integer
    userInput = int(userInput)

    # Check if the guessed number is correct
    if userInput == randomNumber:
        print(f"Congratulations! The number {userInput} is the perfect match.")
        break
    else:
        print(f"You missed by selecting the number ({userInput}). Guess again!")

