# Exercise 10: Factorial Calculation Using a Loop
# Objective: Practice using loops to perform repetitive tasks.

# Exercise: Write a program that calculates the factorial 
# of a given number using a for loop.

# Importing RegEx
import re

# Defined pattern to check import validity
pattern = r'^(0|[1-9][0-9]*)$'

# A note to the user
print("Number must be a positive integer in order to find its factorial succefully!")

# Prompt user to input the number
userInput = input('Enter number here: ')

# Check if number is valid. 
if re.match(pattern, userInput) :
    
       # If "True", change the datatype to ~int
       number = int(userInput)
       
       # Defined a variable to hold the factorial of the input
       factorial = 1
       
       # Loop through the range from 1 to the [input]
       # and perform the arithmetics
       for i in range(1, number + 1) :
           factorial *= i
       
       # Print out the factorial.    
       print(f"The factorial of {userInput} is: {factorial}")

# If input is not valid,
else:
     # Prompt the user.
     print(f"Input invalid! Number must be a positive integer only.")
