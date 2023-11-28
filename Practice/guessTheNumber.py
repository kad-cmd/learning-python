import random

secretnumber = random.randint(1, 10)
print("I am thinking of a number between 1 and 10.")
print("You have 6 tries to guess the number.")

for guesstaken in range(1, 7):
    print("Take a guess. ")
    guess = int(input())

    if guess == secretnumber:
        print(f"Good job! You guessed the number in {guesstaken} guesses.")
        break
    elif guess < secretnumber:
        print(f"Your guess is too low")
        print(" <<<< Tries : " + str(guesstaken) + " >>>> ")
        continue
    elif guess > secretnumber:
        print(f"Your guess is too high")
        print(" <<<< Tries : " + str(guesstaken) + " >>>> ")
        continue
if guesstaken == 6:
    print(f"Nope, The number was {secretnumber}")