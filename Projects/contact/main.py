import os 
import csv
import datetime
#import time import strftime


class person:
    def __init__(self, frst_name, lst_name, pnumber, email):
        self.frst_name = frst_name
        self.lst_name = lst_name
        self.pnumber = pnumber
        self.email = email
    
    
    def __str__(self) -> str: # stores our info, and allows us to display the info.
        return f"{self.frst_name} {self.lst_name}, Number : {self.pnumber}, Email : {email}."
    



def title():
    line_1 = "----------------------------------------------"
    tq      = "Contacts Management System"
    line_2 = "----------------------------------------------"
    print(line_1.center(130))
    print(tq.center(130))
    print(line_2.center(130))


# Using os module we will clear the console and create menu page.
os.system("cls")
title()


contacts = list()
usr_input = ""

while True:
    print("1. Create a contacts".center(129))
    print("2. view your contacts".center(132))
    print("d. delete a contact".center(129))
    print("s. Search Contacts".center(127))
    print("q. Exit the program".center(129))
    print("________________________".center(131))
    usr_input = input("\t\t\t\t\t\t\tSelect options: ")

    if usr_input == "1": # adding a contact
        os.system("cls")
        title()
        with open('contact.txt', 'a') as f:
            print("please enter the contact informations\n")

            first_name = input("First name --> ")
            last_name = input ("Last name --> ")  
            phone_number = input("Number --> ")
            email = input("Email Address --> ")
            f.writelines((first_name, ' : ', last_name, ' : ', phone_number, ' : ', email, '\n'))

            #!!!!! fix this!!!!!
            # its creating two saving the data into two sepate files
        # stores the data into our class
        newContact = person(first_name, last_name, phone_number, email)
        contacts.append(newContact)
        print("Thank you we have received your contact...")
        os.system("cls")
    
    elif usr_input == "2": # display all of our contacts
        os.system("cls")
        title()
        for contact in contacts:
            print(f"[ {contact} ]\n")
            print("----------\n")
            print("_______________________\n")
            print("Press Enter to continue...\n")
            done = input()
            if done == "":
                os.system("cls")
                break

    elif usr_input == "d":
        os.system("cls")
        print("Who do you wish to remove? ")
        p = input
        p = int(contacts.index(p))
        contacts.pop(p)

        # testing
        print(contacts)
    


    elif usr_input == "s":
        pass

    elif usr_input == "q":
        os.system("cls")
        print("Thank You for using our programe")
        break
    
    #this clears the console when the user does not enter anything/ 
    os.system("cls")


# 3. Search for a Contact: Users can search for a contact by name and view their details.


# 4.  Update Contact: Users can update the information (phone number and email) of an existing contact.


# 5.  Delete Contact: Users can delete a contact from the contact book.

