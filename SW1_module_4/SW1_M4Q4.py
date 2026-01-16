import random

guess = int("0")
rngnmb = random.randint(1, 10)
print(rngnmb)

while True:
    guess = int(input("Guess a number (1-10): "))
    if guess < rngnmb:
        print("Too low")
    elif guess > rngnmb:
        print("Too high")
    elif guess == rngnmb:
        print("Correct")
        break