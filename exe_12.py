# 2. Functions
# Exercise 2: Simple Calculator with Functions

# Goal: Create a simple calculator using functions for addition, 
# subtraction, multiplication, and division. The program should ask 
# the user for two numbers and the operation they wish to perform, 
# then call the respective function and print the result.


import re

def add(numb1, numb2) :
    return numb1 + numb2

def substract(numb1, numb2) :
    return numb1 - numb2

def multiply(numb1, numb2) :
    return numb1 * numb2

def divide(numb1, numb2) :
    if numb2 == 0 :
        return "Error! Division by Zero"
    return numb1 / numb2

def calc(statement) :
    valid_numb_pattern = r'^-?\d+(\.\d+)?$'
    valid_operator_pattern = r'^[+\-*/]$'

    values = statement.split(' ')
    
    if len(values) != 3 :
      return f"Error! Statement must have 3 parts. Example: 34.32 + 32"  
  
    numb1,  operator, numb2= values[0], values[1], values[2]
    
    if not re.match(valid_numb_pattern, numb1):
        return "Invalid number: '{}' in statement".format(numb1)
    if not re.match(valid_numb_pattern, numb2):
        return "Invalid number: '{}' in statement".format(numb2)
    if not re.match(valid_operator_pattern, operator):
        return "Invalid operator: '{}' in statement. Use +, -, *, /".format(operator)
    
    
  
    numb1 = float(numb1)
    numb2 = float(numb2)
    match operator :
        case '+' :
             RESULT = add(numb1, numb2)
        case '-' :
              RESULT = substract(numb1, numb2)
        case '*' :
            RESULT = multiply(numb1, numb2)
        case '/' :
               RESULT = divide(numb1, numb2)
    
    return f"Result: {numb1} {operator} {numb2} = {RESULT}"

print("Enter Statement seperated by spaces!. Eg: x + y.z \nAllowed operation - (+, -, *, /)")

# Asking user for input
statement = input('Statement: ')


print(calc(statement))
            
        

    
