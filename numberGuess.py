import random

name = input("Hello there! What is your name?")

print("Hello " + name + "!")
print("I want to play a guessing game")
print("I am thinking of a number between 1 and 10. What number is it?")

guessedNumber = input("Type your number here.")

if (guessedNumber.isdigit()):
    randomNumber = int(random.randrange(1, 10))

    if int(guessedNumber) == randomNumber:
        print("You got it right!")
    elif int(guessedNumber) != randomNumber:
        print("Wrong, it was actually ", randomNumber, ", but good try!")
else:
    print("Error! You need to input a number")