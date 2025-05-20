import random

random_number = random.randint(0, 5)

def guess():
    user_input = int(input("Guess a number: "))

    while user_input != random_number:
        if user_input < random_number:
            user_input = int(input("Too low! Guess again: "))
        if user_input > random_number:
            user_input = int(input("Too high! Guess again:"))
    print(f"{user_input} is correct!")


def guess_2(x):
    random_number = random.randint(1,x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}"))
        if guess < random_number:
            print("Sorry! Guess higher")
        elif guess > random_number:
            print("Sorry. Guess lower ...")
    print("Correct! JACKPOT!!")

guess()
guess_2(5)