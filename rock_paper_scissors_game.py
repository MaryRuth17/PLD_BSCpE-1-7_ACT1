# Rock, Papers, Scissors game

import random

options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)

player = input("Enter a choice (rock, paper, scissors): ")

print(f"Player: {player}")
print(f"Computer: {computer}")

