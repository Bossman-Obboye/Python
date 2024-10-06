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

print("Enter Statement seperated by spaces!. Eg: x + y.z \nNB: Valid operation signs - (+, -, *, /) \n")

statement = input('Statement: ')


def calc(statement) :
    valid_numb_pattern = r'^[+-]?\d*(\.\d+)?$'
    valid_operator_pattern = r'^[+-*/]$'

    values = statement.split(' ')
    
    try :
        numb1 = values[0]
        operator = values[1]
        numb2 = values[2]
    except :
        numb1 = ''
        operator = ''
        numb2 = ''
        return 'Unexpected Error occurred'
        
    print(numb1, numb2, operator)
    
    if not re.match(valid_numb_pattern, numb1):
       return "Invalid Statement, Correct it! Eg: 34.32 + 32"
    elif not re.match(valid_numb_pattern, numb2) :
       return "Invalid Statement, Correct it! Eg: 34.32 + 32"
    elif not re.match(valid_operator_pattern, operator) :
       return "Invalid Statement, Correct it! Eg: 34.32 + 32"
    else :
        numb1 = float(numb1)
        numb2 = float(numb2)
        RESULT = ''
    
        match operator :
            case '+' :
                RESULT = str(add(numb1, numb2))
            case '-' :
                RESULT = str(substract(numb1, numb2))
            case '*' :
                RESULT = str(multiply(numb1, numb2))
            case '/' :
                RESULT = str(divide(numb1, numb2))
    
        return f"RESPONSE: {statement} = {RESULT} \nYou are always welcome."

print(calc(statement))
            
        

    
