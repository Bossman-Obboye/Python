# 3. Data Structures (Lists, Tuples, and Dictionaries)
# Exercise 3: Shopping Cart

# Goal: Write a program that simulates a simple shopping cart. Allow 
# the user to add items to the cart, view the cart, and remove items 
# from the cart.


cart = []


def addItemToCart(item) :
    cart.append(item)
    print("{} has been add to your cart.".format(item))


def viewCartItems():
    if not cart :
        print("Your cart is empty!")
    else:
        print('Your cart contains:')
        for item in cart :
            print(f"- {item}")


def delCartItem(item):
    if not item in cart:
        print(f"Error! Your cart doesn't contain: {item}")
    else:
        cart.remove(item)
        print(f"{item} has been removed from your cart.")


while True:
    
    print("\n1. Add Item to Cart")
    print("2. View Cart Items")
    print("3. Remove an Item")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    
    
    match choice :
        case '1' : 
            item = input("Enter item to be added: ")
            addItemToCart(item)
        case '2' :
            viewCartItems()
        case '3' :
            item = input("Enter item to be removed: ")
            delCartItem(item)
        case '4' :
            break
        case _ :
            print(f"Invalid choice :) => ({choice}). Please try again.")
        