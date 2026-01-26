import random
a = ""
b = ""
c = 0

while c < 3:
    a += str(random.randint(0, 9))
    c = c + 1

c = 0

while c < 4:
    b += str(random.randint(1, 6))
    c = c +1

print("3-digit code:", a)
print("4-digit code:", b)