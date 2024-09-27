# Exercise: Write a program that asks the user for a string 
# and counts the number of vowels (a, e, i, o, u) in the string.

import re

# Accepting Input from the User
dataFromUser = input("Enter 'String' to be checked: ")

# Pattern of Vowels to use for the check
pattern = r'[aeiouAEIOU]'

# Create a list of the vowels in the user's input
vowelsInDataFromUser = re.findall(pattern, dataFromUser)

# Find the number of vowels and assign it to "count"
count = len(vowelsInDataFromUser)

# Print the result
print(f"The number of vowels in the 'String' you provided is: {count}")
