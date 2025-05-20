import random

random_number = random.randint(0, 100)

def guess():
    user_input = input("Guess a number: ")

    while user_input != random_number:
        if int(user_input) < random_number:
            user_input = input("Too low! Guess again: ")
        if int(user_input) > random_number:
            user_input = input("Too high! Guess again:")
        if int(user_input) == random_number:
            print("{user_input} is correct!".format())
guess()