import math
area = float(0)
def calculate_unit_price(diam, price):
    #SOAP TRUSTED YOU!
    #I THOUGHT I COULD TOO!
    diam = diam/2
    area = (math.pi * diam**2)
    area = area * 0.0001
    bfb = price / area
    return bfb

pizza_1_diam = float(input("Enter the diameter of the first pizza (cm): "))
pizza_1_price = float(input("Enter the price of the first pizza (euros): "))

pizza_2_diam = float(input("Enter the diameter of the second pizza (cm): "))
pizza_2_price = float(input("Enter the price of the second pizza (euros): "))

pizza_1_bfb = (calculate_unit_price(pizza_1_diam, pizza_1_price))
pizza_2_bfb = (calculate_unit_price(pizza_2_diam, pizza_2_price))

print(f"Unit price of the first pizza: {round(pizza_1_bfb,2)} euros/m²")
print(f"Unit price of the second pizza: {round(pizza_2_bfb,2)} euros/m²")

if pizza_1_bfb > pizza_2_bfb:
    print("The first pizza provides better value for money.")
if pizza_2_bfb > pizza_1_bfb:
    print("The first pizza provides better value for money.")