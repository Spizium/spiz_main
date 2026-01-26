import random

a = int(input("Tahko: "))

def roll_dice(a):
    return random.randint(1, a)

b = 0

while a != b:
    b = roll_dice(a)
    print(b)
