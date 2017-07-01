import random  # Imports the built-in random module.
# This is a guessing game, the computer chooses a random number between 1 and 20 and the user has 6 rounds to guess it.
guessesTaken = 0  # Assigns the 0 value to guessesTaken variable (integer).

print('Hello! What is your name?')  # Prints out the string between parentheses to console, starts a new line.
myName = input()  # Waits for input from user, stores it as a string in myName variable.

number = random.randint(1, 20)  # Assigns a pseudo random integer between the arguments (1, 20) to number variable using the imported randint function of random module.
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # Prints out the string between parentheses to console, and replaces the variable with its value.

while guessesTaken < 6:  # Repeats the indented code while the value of guessesTaken is smaller than 6.
    print('Take a guess.')  # Prints out the string between parentheses to console, starts a new line.
    guess = input()  # Waits for input from user, stores it as a string in guess variable.
    guess = int(guess)  # Converts (casts) the value of guess variable (string) into integer.

    guessesTaken += 1  # Increases the value of guessesTaken by 1.

    if guess < number:  # Decides if the value of guess is less than the value of number, executes the indented code below if it's true.
        print('Your guess is too low.')  # Prints out the string between parentheses to console, starts a new line.

    if guess > number:  # Decides if the value of guess is more than the yalue of number, executes the indented code below if it's true.
        print('Your guess is too high.')  # Prints out the string between parentheses to console, starts a new line.

    if guess == number:  # Decides if the value of guess variable is equal to the value of number variable, executes the indented code below if it's true.
        break  # Breaks out from the while loop.

if guess == number:  # Decides if the value of guess variable is equal to the value of number variable, executes the indented code below if it's true.
    guessesTaken = str(guessesTaken)  # Converts (casts) the value of guessesTaken variable (integer) into string.
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')  # Prints out the string between parentheses to console, and replaces the variables with its value.

if guess != number:  # Decides if the value of guess variable is not equal to the value of number variable, executes the indented code below if it's true.
    number = str(number)  # Converts (casts) the value of number variable (integer) into string variable.
    print('Nope. The number I was thinking of was ' + number)  # Prints out the string between parentheses to console, and replaces the variable with its value.
