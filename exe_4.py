
# Exercise: Write a simple calculator program that asks the user for 
# two numbers and an operator (+, -, *, or /) and then performs the 
# corresponding calculation and displays the result.

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
operator = input("Enter an operator: ")

if operator == "+" :
    print(f"{num1} + {num2} = {int(num1) + int(num2)}")
elif operator == "-" :
     print(f"{num1} - {num2} = {int(num1) - int(num2)}")
elif operator == "/" :
     print(f"{num1} - {num2} = {int(num1) / int(num2)}")
elif operator == "*":
     print(f"{num1} x {num2} = {int(num1) * int(num2)}")
else :
    print('Error occurred. Please check your inputs and try again.')