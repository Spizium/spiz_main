import random

rolls = int(input("How many dice to roll: "))
dicesum = int(0)

for n in range(rolls):
    dicesum += random.randint(1,6)

print(f"Sum of the dice: {dicesum}")
