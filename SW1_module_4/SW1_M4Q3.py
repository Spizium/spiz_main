nmbrlist = []
nmbr = int()
listcount = int(0)


while True:
    listcount += 1
    nmbr = input("Enter a number (or press Enter to quit): ")
    if nmbr == "":
        nmbrlist = [int(x) for x in nmbrlist]
        listcount += -1
        break
    nmbrlist.append(nmbr)

a = sorted(nmbrlist)
lenz = len(nmbrlist)
print(f"Smallest number: {a[0]:.1f}")
print(f"Largest number: {int(a[lenz-1]):.1f}")
