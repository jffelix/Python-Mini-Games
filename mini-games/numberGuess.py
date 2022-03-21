import random

name = input("Hello there! What is your name?")

print("Hello " + name + "!")
print("I want to play a guessing game")

while True:

    print("I am thinking of a number between 1 and 5. What number is it?")

    guessedNumber = input("Type your number here.")

    if (guessedNumber.isdigit()):
        randomNumber = int(random.randrange(1, 6))

        if int(guessedNumber) == randomNumber:
            print("You got it right!")
        elif int(guessedNumber) != randomNumber:
            print("Wrong, it was actually ", randomNumber, ", but good try!")
    else:
        print("Error! You need to input a number!")

    print("Play again? (y/n)")
    response = input("Type 'y' or 'n'.")

    if response.lower() == "y":
        print("____________________________________________________________________")
        continue
    elif response.lower() == "n":
        print("Thanks " + name +  " for playing!")
        break
    else:
        print("Invalid input. You need to choose 'y' or 'n'.")
        break