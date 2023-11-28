import random
import os

digit = 3
trys = 10

def main():
    os.system('cls')
    print(''' I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.'''.format(digit))

    while True: #Main game loop # Stores the secret number
        secretNum = getSecret()
        print(" ")
        print("I though of a number...")
        print("You have {} guesses to get it".format(trys))

        numGuess = 1
        while numGuess <= trys:
            guess = ''
            # Loop til' usr enters a valid Num.
            while len(guess) != digit or not guess.isdecimal():
                print("Guess #{}".format(numGuess))
                guess = input("> ")
            
            clue = getClues(guess, secretNum)
            print(clue)
            numGuess += 1

            if guess == secretNum:
                break # The user entered the secretNumber.
            if numGuess > trys:
                print("You have used up all of your {} trys".format(trys))
                print("{} was the Secret number".format(secretNum))

        # ask the user if they want to play again.
        print("Do you wish to play again? (y/n): ")
        if not input('> ').lower().startswith('y'):
            break # The user entered No
    print("Thank you for playing")

def getSecret():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789')  # Create a list of digits 0 to 9.
    random.shuffle(numbers)  # Shuffle them into random order.

    # Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ''
    for i in range(digit):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    if guess == secretNum:
        return "you got it"

    
    clue = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct Digit is in the correct place
            clue.append('Fermi')
        elif guess[i] == secretNum:
            # incorect digit
            clue.append("pico")
    if len(clue) == 0:
        return 'bagels' # There are no correct digits at all.
    else:
        clue.sort()
        return ''.join(clue)

if __name__ == '__main__':
    main()