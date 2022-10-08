from random import seed
from random import randint


def takeInput():
    inputthis = int(input("Guess the number 0- 10: "))
    return inputthis


def randomNum():

    seed(1)
    value = randint(0, 10)
    print("The random value is " + str(value))
    "userGuess = takeInput()"
    "computerGuess = ComputerGuess()"
    computerguess = randint(0, 10)

    while computerguess != value:
        if computerguess < value:
            print("Too low")
            "userGuess = takeInput()"
            computerguess = randint(computerguess, 0)
            print(f"The computer guessed {computerguess}")
        elif computerguess > value:
            print("Too high")
            "userGuess = takeInput()"
            computerguess = randint(0, computerguess)
            print(f"The computer guessed {computerguess}")
    else:
        print("The Computer guessed correctly")


randomNum()