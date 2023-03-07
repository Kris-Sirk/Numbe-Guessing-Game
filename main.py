# Author: Chris.K


# Guess the Number Game: Create a game where the computer generates a random number
# and the user has to guess the number within a certain number of tries. The program
# should give hints such as "higher" or "lower" to help the user guess the number.

import random

print("Welcome to the random number game!")
print("A random number between 0 and 1000 has been generated.")
mystery = random.randint(0, 1000)
for guess in range(100):
    inp = int(input("Please insert your guess:"))
    if inp == mystery:
        print("Well done, you guessed the correct number!")
        break
    elif abs(inp - mystery) <= 25:
            if inp > mystery:
                print("Your getting close, just a little lower!")
            else:
                print("Your getting close, just a little higher!")
    elif inp > mystery:
        print("The number you guessed is higher than the mystery number!")
    elif inp < mystery:
        print("The number you guessed is lower than the mystery number!")



