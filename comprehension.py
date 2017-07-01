import random  # Imports the built-in random module.

guessesTaken = 0  # Assigns the 0 value to guessesTaken variable (integer).

print('Hello! What is your name?')  # Prints out on standard output the message: 'Hello! What is your name?' and starts a new line.
myName = input()  # Waits for input from user, stores it as a string in myName variable. The input should be the name of the user.

number = random.randint(1, 20)  # From imported random module uses the randint function, which gives back a random integer between the arguments (1->20).
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # Prints out on standard output the message: 'Well, *myName*, I am thinking of a number between 1 and 20.', where *name* is the value of the myName variable.

while guessesTaken < 6:  # Loops while guessesTaken is smaller than 6. If this is true the commands written indented under the while loop will execute.
    print('Take a guess.')  # Prints out on standard output the message: 'Take a guess.'
    guess = input()  # Waits for input from user, stores it as a string in guess variable. The input should be the guess of the user.
    guess = int(guess)  # Converts (casts) the value of guess variable (string) into integer. If the guess variable is not a number the program raises an ValueError.

    guessesTaken += 1  # Increases the value of guessesTaken by 1.

    if guess < number:  # Decides if the value of guess variable is less than the value of number variable. If this is true the commands written indendted under the if statement will execute.
        print('Your guess is too low.')  # Prints out on standard output the message: 'Your guess is too low'.

    if guess > number:  # Decides if the value of guess variable is more than the value of number variable. If this is true the commands written indendted under the if statement will execute.
        print('Your guess is too high.')  # Prints out on standard output the message: 'Your guess is too high'.

    if guess == number:  # Decides if the value of guess variable is equal than the value of number variable, meaning the user's guess was right. If this is true the commands written indendted under the if statement will execute.
        break  # Breaks out from the while loop starting at the line 11, meaning the loop will stop executing.

if guess == number:  # Decides if the value of guess variable is equal to the value of number variable, meaning the user's guess was right. If this is true the commands written indendted under the if statement will execute.
    guessesTaken = str(guessesTaken)  # Converts (casts) the value of guessesTaken variable (integer) into string.
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')  # Prints out on standard output the message: 'Good job, *myName*! You guessed my number in *guessesTaken* guesses!', where the *myName* is replaced with the value of myName variable, while the *guessesTaken* is replaced with the value of guessesTaken variable.

if guess != number:  # Decides if the value of guess variable is not equal to the value of number variable, meaning the user's guesses were all wrong. If this is true the commands written indendted under the if statement will execute.
    number = str(number)  # Converts (casts) the value of number variable (integer) into string variable.
    print('Nope. The number I was thinking of was ' + number)  # Prints out on standard output the message: 'Nope. The number I was thinking of was *number*', where the *number* is replaced with the value of the number variable.
