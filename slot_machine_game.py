# Slot Machine Game 

import random

def spin_row():
    symbols = ['💖', '🎉', '🌹', '💋']

    return [random.choice(symbols) for _ in range(3)]

def print_roe():
    pass

def get_payout():
    pass

def main():
    balance = 100

    print("-----------------------")
    print("welcome to mary machine")
    print("Symbols: 💖 🎉 🌹 💋")
    print("------------------------")

    while balance > 0:
        print(f"Current balance: ${balance}")

        bet = input("Place your bet: ")

        if not bet.isdigit():
            print("please enter valid amount")
            continue

        bet = int(bet)

        if bet > balance:
            print("invalid amount")
            continue

        if bet <= 0:
            print("invalid amount")
            continue

        balance -= bet

        row = spin_row()
        print(row)

if __name__ == '__main__':
    main()