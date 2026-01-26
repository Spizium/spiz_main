import math
nmbr = int(input("Enter an integer: "))

if (nmbr > 1 and all(nmbr % i != 0 for i in range(2, int(math.sqrt(nmbr)) + 1))) == True:
    print(f"{nmbr} is a prime number.")
elif (nmbr > 1 and all(nmbr % i != 0 for i in range(2, int(math.sqrt(nmbr)) + 1))) == False:
    print(f"{nmbr} is not a prime number.")
