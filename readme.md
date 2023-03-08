## Author
Chris K.

## Random Number Game
This is a simple Python game that generates a random number between 0 and 1000, and prompts the user to guess the number. The game provides feedback to the user based on the guess, and ends when the user guesses the correct number, or has made 100 incorrect guesses.

## How to play
* Run the script in a Python environment.
* The game will generate a random number between 0 and 1000.
* The user will be prompted to guess the number.
* The user has up to 100 attempts to guess the number correctly.
* If the user guesses the correct number, the game will end and print a congratulatory message.
* If the user's guess is within 25 of the mystery number, the game will provide a hint to help the user guess the number.
* If the user's guess is incorrect and not within 25 of the mystery number, the game will provide feedback indicating whether the guess is too high or too low.
* If the user has made 100 incorrect guesses, the game will end.
## Code structure
The code uses a for loop to allow the user up to 100 attempts to guess the number. The random module is used to generate a random integer between 0 and 1000, and the input() function is used to get the user's guess. The code then uses a series of if statements to provide feedback to the user based on the guess.

## How to customize
If you want to change the range of the random 
number generated, you can modify the arguments
to `random.randint()`. For example, if you want 
to generate a random number between 0 and 100,
you can use `random.randint(0, 100)`.

If you want to change the number of attempts
allowed, you can modify the range of the for
loop. For example, if you want to allow the 
user 50 attempts, you can use `for guess in 
range(50):`.
