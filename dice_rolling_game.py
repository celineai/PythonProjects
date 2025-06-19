"""
Part of Programming with Mosh's Python Projects Tutorial.
"""

import random

while True:
    # ask the user to roll the dice
    consent = input("Roll the dice? (y/n): ").lower()
    if consent == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'({die1}, {die2})')
    elif consent == 'n':
        print("Thanks for playing!")
        break
    else:
     print("Invalid choice!")
