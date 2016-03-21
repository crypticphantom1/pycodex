#game made from nothing (higher and lower game)
#21/03/16

import random

counter = 0
my_random_number = random.randint(1, 10)

guess = int(input("what is your guess? "))
counter = counter + 1

while guess != my_random_number:
    if guess < my_random_number:
        print("try higher")
    else:
        print("try lower")
    guess = int(input("what is your guess? "))
    counter = counter + 1

print("yay you win! it took you " + str(counter) + " guesses.")
