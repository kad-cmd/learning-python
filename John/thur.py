x = input("Enter a number: ")
y = input("Enter another number: ")

# Operators
print("<<< Enter an operator! >>>")
print("[a]'add', [s]'subtract', [m]'multiply' or [d]'divide'")
operation = input()

# if statements
if operation == "a":
    print(int(x) + int(y))
elif operation == "s":
    print(int(x) - int(y))
elif operation == "m":
    print(int(x) * int(y))
elif operation == "d":
    print(int(x) / int(y))
else:
    print("Invalid operator!")
    print("Try again!")