#  Exception Handling
# Exercise 5: Division Calculator with Error Handling
# 
# Goal: Write a program that takes two numbers from the user and 
# performs division. Implement error handling to manage invalid 
# input (non-numeric values) and division by zero.
# 
# Hints:
# 
# Use try-except blocks to handle ValueError (invalid input) and 
# ZeroDivisionError.


try :
    num1 = float(input('Enter first number: '))
    num2 = float(input("Enter second number: "))
    result = num1/num2

except ValueError :
    print('Error! Enter valid numbers')
except ZeroDivisionError :
    print('Error! Division by Zero is not allowed.')
else :
    print(f"The result is: {result}")
finally :
    print("Operation completed\n")