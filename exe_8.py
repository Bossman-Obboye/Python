# Exercise: Write a program that asks the user for a string 
# and counts the number of vowels (a, e, i, o, u) in the string.

import re

dataFromUser = input("Enter 'String' to be checked: ")

pattern = r'[aeiouAEIOU]'
vowelsInDataFromUser = re.findall(pattern, dataFromUser)

print(f"The number of vowels in the 'String' you provided is: {len(vowelsInDataFromUser)}")
