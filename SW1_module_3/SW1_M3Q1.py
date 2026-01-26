f = float(input("Enter the length of the zander in centimeters: " ))

if f < 42:
    print("The zander does not meet the size limit.")
    print("Please release the fish back into the lake.")
    print("The fish was",round(42-f,2),"centimeters below the size limit.")
else:
    print("The zander meets the size limit.")