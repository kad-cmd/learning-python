'''
# Multi player game

    Everyone gets a turn, comes your turn u get to roll a dice, you're going to get some number from 1 to 6.
    if you get anything other than one, you take that and you add that to the score of your turn.

    So let's say you get a five, now you're at five. Roll it again, you get another five, you're at ten, 
    and you can decide how many times you want to roll the dice.

    the catch is as soon as you hit a one, whatever you got on your role is going to be done.
    Whatever you got on your turn is is zero. 

    you completely remove the score so you can roll five times, three times, four
    times, ten times, 20 times as much as you want. But every additional roll you're gambling the possibility
    of losing your score. 

    So you need to decide when you want to stop. As soon as you stop whatever your current score
    is, assuming it's not zero, is going to get added to your total score. And then you can determine the number of total rolls
    you want to have, or it's whoever reaches like 101st. Or 51st. Whatever you want to do. And our case will say like
    the max score is something like 50. Whoever hits 51st is the winner of the game.

'''


import random
import os

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value) # generates the random number between 1 - 6

    return roll

os.system("cls")
while True:
    players = input("Enter the numbers of players (1-4): ")


    if players.isdigit(): # Checks if the input(*str) is a valid number and the it will converte it to an int.
        players = int(players)
        if 2 <= players <= 4: # checks if players exceeds the max or not
            break
        else:
            print("Must be between 2-4 players.")

    else:
        print("Invalid, Try again.")

max_score = 50
player_scores = [0 for _ in range(players)] # list comprehension, # puts a zero for evry player

while max(player_scores) < max_score:
    for player in range(players): # one player
        print("\nPlayer #", player + 1, "turn has just started!")
        print("Your total score is :", player_scores[player], "\n")
        current_score = 0 
        while True:
            should_roll = input("Would you like to roll (y)?: ")
            if should_roll.lower() != "y":
                break

            value = roll() # if they wanna roll again, we call the roll function

            if value == 1: # when they roll 1, their score will be 0
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a: {value}.")

            print(f"Your score is: {current_score}")
            
        os.system("cls")
        player_scores[player] += current_score # adds the final score to score board.
        print(f"player #{player + 1} Your current score is: {player_scores[player]}")
        

# checks to see who had point<50 first and then prints the winner
max_score = max(player_scores)
winner = player_scores.index(max_score)
print("player #", winner + 1, "is the winner with a score of:", max_score)