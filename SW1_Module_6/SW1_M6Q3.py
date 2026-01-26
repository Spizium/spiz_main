gallons = 1

def gallons_to_liters(gallons):
    return (gallons * 3.785)

while True:
    gallons = float(input("Enter a volume in American gallons (negative value to quit): "))
    if gallons > 0:
        print(f"{gallons} American gallons is {round(gallons_to_liters(gallons),2)} liters.")
    if gallons < 0:
        print("Program finished.")
        break

