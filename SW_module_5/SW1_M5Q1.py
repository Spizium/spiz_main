import random

rolls = int(input("How many dice to roll: "))
rolled = []
dice = int(0)

for n in range(rolls):
    dice = random.randint(1, 6)
    rolled.append(dice)

dicesum = int(0)
for rolled in range(rolls-1):
    dicesum += n

print(f"Sum of the dice: {dicesum}")