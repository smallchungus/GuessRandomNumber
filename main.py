from random import seed
from random import randint


def takeInput():
    inputthis = int(input("Guess the number 0- 10: "))
    return inputthis


def randomNum():

    seed(1)
    value = randint(0, 10)
    print("The random value is " + str(value))
    userGuess = takeInput()

    while userGuess != value:
        if userGuess < value:
            print("Too low")
            userGuess = takeInput()
        elif userGuess > value:
            print("Too high")
            userGuess = takeInput()
    else:
        print("You guessed correctly")

randomNum()