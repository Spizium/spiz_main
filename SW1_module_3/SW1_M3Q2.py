boat = input("Enter the cabin class (LUX, A, B, or C): ")


if boat == str("LUX"):
    print("Upper-deck cabin with a balcony.")
elif boat == str("A"):
    print(" Above the car deck, equipped with a window.")
elif boat == str("B"):
    print("Windowless cabin above the car deck.")
elif boat == str("C"):
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")
