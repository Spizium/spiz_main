talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

total_grams = (talents * 20 * 32 * 13.3) + (pounds * 32 * 13.3) + (lots * 13.3)
kilograms = int(total_grams/1000)
remaining_grams = (((total_grams/1000)-kilograms)*1000)
remaining_grams = round(remaining_grams, 2)

print("The weight in modern units:")
print(kilograms,("kilograms and"),remaining_grams,("grams."))
