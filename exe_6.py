# Exercise: Write a program that takes a list of five names as 
# input and then prints each name in uppercase.

# List to store the names
list_of_names = []

# Utils -- Positions
list_of_state = ('first', 'second', 'third', 'forth', 'last')

# By iterating within the range of 5, accept, convert and assign 
# all the names to 'list_of_names'
for i in range(5) :
    # Accept name
    name = input(f"Enter {list_of_state[i]} person's name here: ")
    
    # Convert to uppercase
    name = name.upper()
    
    # Assign name
    list_of_names.append(name)

print('These are the names in uppercases: ')
for i in list_of_names:
    print(i)
