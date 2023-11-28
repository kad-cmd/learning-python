def main():
    x = input("Enter a number: ")
    y = input("Enter another number: ")
    while True:
        print(" [a]'add', [s]'subtract', [m]'multiply' or [d]'divide'")
        operation = input()
        if operation == "a":
            a = float(x) + float(y)
            print(a)
            break
        elif operation == "s":
            s = int(x) - int(y)
            print(s)
            break
        elif operation == "m":
            m = float(x) * int(y)
            print(m)
            break
        elif operation == "d":
            d = float(x) / float(y)
            print(d)
            break
        else:
            print("Invalid Operation!")
            continue
main()