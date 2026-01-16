a = float("1")

while True:
    a = float(input("Enter length in inches (negative value to quit): "))
    if a < 0:
        print("Program ended.")
        break
    print(f"{a} inches is {a*2.54:.2f} centimeters")
