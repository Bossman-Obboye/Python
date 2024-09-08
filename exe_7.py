# Exercise: Write a program that asks the user to input a list
# of numbers and then prints the largest number in the list.

# Container to store the numbers
numList = []

# Notify and accept list
print("Enter numbers separated by space.")
data = input("List: ")

# Split input string into a list of values
data = data.split()

# Check if all elements are numbers
try:
    for i in data:
        # Convert to float and append to list
        numList.append(float(i)) 
    # Print the highest value using max() function
    print(f'The highest value in the list is: {max(numList)}')
except ValueError:
    print('List contains a non-numeric value, please check input and try again!')
