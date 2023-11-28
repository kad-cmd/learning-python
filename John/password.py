while True:
    x = "johntheguy"
    print("Enter a password: ")
    y = input()

    if x == y:
        print("You are logged in!")
        break
    else:
        print("Wrong password. Try Again!")
        continue