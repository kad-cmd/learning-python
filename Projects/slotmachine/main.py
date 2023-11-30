import random

MAX_LINES = 3 # all capitals because this is a constant value is something thats not going to change.
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    for line in range(lines):
        pass # following https://www.youtube.com/watch?v=th4OBktqK1I&ab_channel=TechWithTim  where : 40:27


def get_slot_machine_spin(ROWS, COLS, symbol):
    all_symbols = []
    for symbol, symbol_count in symbol.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(COLS):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(ROWS):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        
        columns.append(column)
        
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns): # enumerate gives you the index of the item in the list
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
                
        print()


def deposit():
    while True:
        amount = input("How much money do you want to deposit? $")
        if amount.isdigit(): # checks if the input is a digit
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("please enter a digit.")
    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet in (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit(): # checks if the input is a digit
            lines = int(lines)
            if 1 <= lines <= MAX_LINES: # checks if the input is a number between 1 and MAX_LINES
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("please enter a digit.")
    return lines


def get_bet():
    while True:
        bet = input("How much do you want to bet on each line? $")
        if bet.isdigit(): # checks if the input is a digit
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET: # checks if the input is a number between MIN_BET and MAX_BET
                break
            else:
                print(f"amount must be between ${MIN_BET} and ${MAX_BET}")
        else:
            print("please enter a digit.")
    return bet


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_balance = bet * lines
        
        if total_balance > balance:
            print(f"You do not have enough money to bet ${bet} on {lines} lines, your current balance is ${balance}")
        else:
            break
        
    print(f"You are betting {bet} dollars on {lines} lines. Total your balance is ${total_balance}")
    
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    
    
    
main()