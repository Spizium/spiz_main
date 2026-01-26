nmbr_ipt = ""
nmbrlist = []
nmbrlist2 = []
lemmings = int("0")
testlist = ["Slop", "Lifeslop", "Lifegem", "Reddith"]

while True:
    nmbr_ipt = input("Enter a number: ")
    nmbrlist.append(nmbr_ipt)
    if nmbr_ipt == "":
        nmbrlist.pop(len(nmbrlist)-1)
        nmbrlist = [float(x) for x in nmbrlist]
        nmbrlist.sort(reverse=True)
        print("The greatest numbers in descending order:")
        break

for i in range(5):
    try:
        print(nmbrlist[i])
    except IndexError:
        pass