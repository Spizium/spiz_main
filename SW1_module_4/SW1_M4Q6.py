import random

#random_float = random.random()
#print(f"Random float between 0.0 and 1.0: {random_float}")

regencount = int(input("Amount of generated coordinates"))
regentries = int("0")
generate = []
regenlist = []
checknmbr = int(-1)
passed = int(0)


while regentries < regencount:
    regentries += 1
    generate = [random.uniform(-1, 1),random.uniform(-1, 1)]
    regenlist.append(generate)

for n in regenlist:
    checknmbr += 1
    if ((regenlist[checknmbr][0])**2 + (regenlist[checknmbr][1])**2) < 1:
        passed += 1

approxpii = float((4*passed)/regencount)

print(f"Approximation of pi: {approxpii}")
