import random

first_roll = random.randint(1,6)
second_roll = random.randint(1,6)
comp_sum = first_roll + second_roll

guess = int(input("Guess the sum of the two dice: "))

if guess == comp_sum:
    result = "win"
else:
    result = "lose"

    print(f"Your guess was {guess} and the sum of the computers two rolls was {comp_sum}. You {result}.")