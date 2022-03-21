import random

print("Welcome! What is your name?")
name = input("Enter your name here.")

print("Hello " + name + "!")
print("Let's play some rock paper scissors.")
print("Type what you have in mind and we'll see who wins!")

while True:

    choices = ['r', 'p', 's']

    playerChoice = input("Type 'r', 'p', or 's' and hit 'Enter'.")

    randomNum = random.randrange(0, 3)
    computerChoice = choices[randomNum]

    if playerChoice == "r" and computerChoice == "p":
        print("I chose paper, and paper beats rock. I win!")
    if playerChoice == "r" and computerChoice == "r":
        print("Looks like we both chose rock. Stalemate!")
    if playerChoice == "r" and computerChoice == "s":
        print("I chose scissors. Darn, you win this one!")
    if playerChoice == "s" and computerChoice == "p":
        print("Your scissors cut through my paper. You win!")
    if playerChoice == "s" and computerChoice == "r":
        print("My rock breaks your scissors. You lose!")
    if playerChoice == "s" and computerChoice == "s":
        print("Looks like we both chose scissors. Stalemate!")
    if playerChoice == "p" and computerChoice == "p":
        print("Looks like we both chose paper. Stalemate!")
    if playerChoice == "p" and computerChoice == "r":
        print("Paper beats rock. You win!")
    if playerChoice == "p" and computerChoice == "s":
        print("My scissors cuts through your paper You lose!")
    

    print("Great game! Play again? (y/n)")
    response = input("Type 'y' or 'n'.")

    if response.lower() == "y":
        continue
    elif response.lower() == "n":
        print("Thanks " + name +  " for playing!")
        break
    else:
        print("Invalid input. You need to choose 'y' or 'n'.")
        break