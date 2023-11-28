# modules
import random # getting the blender
import string 
import os

def generator(min_length, numbers=True, special_characters=True):
    alph = string.ascii_letters
    num = string.digits
    special = string.punctuation

    characters = alph
    if numbers:
        characters += num
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_num = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in num:
            has_num = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_num
        if special_characters:
            meets_criteria = meets_criteria and has_special
        
    return pwd
os.system("cls")


line_1 = "----------------------------------------------"
tq      = "Password Generator System"
line_2 = "----------------------------------------------"
print(line_1.center(130))
print(tq.center(130))
print(line_2.center(130))

print("Welcome to password generator!!!!".center(130))
print("y. Create a password".center(129))
print("v. view your passwords".center(132))
print("d. Delete a password".center(129))
print("n. Exit the program".center(129))
print("________________________".center(131))
choice = input("\t\t\t\t\t\t\tSelect (y,v,d,n): ")


while choice == "y":
    with open('pwd database.txt', 'a') as p:
        os.system("cls")
        min_length = int(input("Enter the minimum length: "))
        os.system("cls")
        has_num = input("Do you want to have numbers (y/n)?: ").lower() == "y"
        os.system("cls")
        has_special = input("Do you want to have special characters (y/n)?: ").lower() == "y"
        os.system("cls")
        pwd = generator(min_length, has_num, has_special)
        print("_______________________________________________".center(130))
        print(f"The generated password is : {pwd}".center(130))
        print("_______________________________________________".center(130))
        p.writelines((pwd, '\n'))
        
        again = input("Do you want to generate another password? (y/n): ").lower()

        if again == "y":
            continue
        else:
            break

os.system("cls")
print("Thank you!!")

### working on 
if choice == 'v':
    with open('pwd database.txt', 'r'):
        print("passwords")