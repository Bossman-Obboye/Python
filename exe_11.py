# 1. Control Structures and Loops
# Exercise 1: Number Guessing Game with Limited Attempts

# Goal: Write a program that generates a random number between 
# 1 and 20. The user has 5 attempts to guess the number. After each guess, 
# the program should inform the user if the guess was too high, too low, 
# or correct. If the user runs out of attempts, the game ends.

import random
import re

# Pattern to check the validation of user's input
pattern = r'^(0|[1-9]|[1][0-9]|20)$'

# The Magic Number
magicNumber = random.randrange(0,21)

# A note to the user.
print('GUESS RIGTH! \nChoose any number(integer) ranging from 0 to 20. Good luck \n')

# The range of attempts
attempts = 5

# For Loop
for attempt in range(attempts):
    # Accept input
    guess = input(f"Choose your number(0-20): ")
  
    # Check the validation of inputs
    while True :
        if not re.match(pattern, guess):
            print(f"{guess} isn't valid, please enter a valid number(1-20)")
            guess = input(f"Choose your number(0-20): ")
        else :
            break
    # Convert input to {int} data-type   
    guess = int(guess)
    
    # Conditional statements to tell when user is right.
    if guess > magicNumber :
        print(f"Wrong Choose There! \n{guess} is slightly greater than the magic number. \nYou have {attempts - attempt - 1} attempts left")
        continue
    elif guess < magicNumber :
        print(f"Wrong Choose There! \n{guess} is slightly less than the magic number. \nYou have {attempts - attempt - 1} attempts left")
        continue
    else :
        print(f"You deserve a flower! \n{guess} is the magic number")
        break
# Tell the magic number if user is unable to determine it.   
if guess != magicNumber: print(f"The magic number was: {magicNumber} \nBetter luck next time")
        
        






