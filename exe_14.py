# Exercise 4: Contact Manager
# 
# Goal: Create a program that allows the user to store contact 
# information (name, phone number) in a file. The user can add 
# new contacts and view existing contacts from the file.
# 
# Hints:
# 
# Use a text file to store contacts (contacts.txt).
# Each contact should be stored on a new line in the format: Name: PhoneNumber.
# Use file handling to read and write data.

def addContact():
    with open('contact.txt', 'a') as file:
        c_name = input("Enter contact's name: ")
        c_phone = input("Enter contact's phone number: ")
        file.write(f"{c_name} : {c_phone}\n")
        print("Contact Saved!")
        
def viewContact():
    try:
        with open('contact.txt') as file:
            contacts = file.readlines()
            if contacts:
                print('Your contacts')
                for contact in contacts:
                    print(contact.strip())
            else:
              print('No contact found!')
    except FileNotFoundError:
        print("No contacts found! Starting adding...")
        

while True:
    print('\n1. Add new contact')
    print('2. View all contacts')
    print('3. Quit')
    
    choice = input('Enter your choice: ')
    
    match choice:
        case '1' :
            addContact()
        case '2' :
            viewContact()
        case '3' :
            break
        case _ :
            print("Invalid choice!")
    
    
