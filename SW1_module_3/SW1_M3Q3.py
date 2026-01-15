sex = input("Enter biological gender (male/female): ")
sex = sex.lower()
#It is called biological sex, not gender.
hbv = float(input("Enter hemoglobin value (g/l): "))


if sex == str("female"):
    if hbv < 117:
        print("Your hemoglobin is low.")
    elif hbv >= 117 and hbv < 155:
        print("Your hemoglobin is normal.")
    elif hbv > 155:
        print("Your hemoglobin is high.")

elif sex == str("male"):
    if hbv < 134:
        print("Your hemoglobin is low.")
    elif hbv >= 134 and hbv < 167:
        print("Your hemoglobin is normal.")
    elif hbv > 167:
        print("Your hemoglobin is high.")
else:
    print("Invalid gender.")