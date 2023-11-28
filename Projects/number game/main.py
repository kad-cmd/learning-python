import random

TRIES = 10

def main():
    secretNum = getNum() # asks the user the defficult, and returns a secret num.

    rules = print(f'''
        Rule:

            1) You will have {TRIES} tries!
            2) good luck!:)

        Levels:
            Easy : between 1 and 20
            Medium : between 1 and 30
            Hard : between 1 and 50
            Crazy : between 1 and 200

    ''')

    goes = 0

    for q in range(TRIES):
        print(f"Guess #{q + 1}")
        guess = int(input())
        if guess == secretNum:
            print(f"You Guessed the correct Number! in {goes} tries")
            break
        else:
            print(getClue(guess, secretNum))
            goes += 1
            continue
    
    print("play again?")
    answer = input()

    if answer != "y":
        quit()
    else:
        main()




def getClue(x, y):
    if int(x) > y:
        return "lower"
    else:
        return "higher"


# ask user the level of defficult
def getNum():
    level = input("Defficulty: (E - 'easy', M - 'Medium', H - 'Hard',C - 'Crazy') ")

    if level.lower() == "E":
        level = random.choice(range(1, 21))
        return level
    elif level.lower() == "M":
        level = random.choice(range(1, 31))
        return level
    elif level.lower() == "H":
        level = random.choice(range(1, 51))
        return level
    elif level.lower() == "C":
        level = random.choice(range(1, 201))
        return level

main()