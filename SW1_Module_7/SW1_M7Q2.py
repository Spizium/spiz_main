# nimet = set()
# nimet.add("Viivi")
# print(f"{nimet}")

names = set()
nimi = 2

while True:
    nimi = str(input("Anna nimi"))
    #Its da break gang B)
    if nimi == "":
        break
    elif nimi in names:
        print("Existing name")
    else:
        print("New name")
    names.add(nimi)

print(f"{names}")
