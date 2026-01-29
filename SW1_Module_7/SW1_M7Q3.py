# Variables
airports = {}
selector = ""
search = ""

# Dictionary-function
def data_compiler(apid,apnm):
    list = {}
    list[apid] = apnm
    return list

# Main-software
while True:
    print("")
    print("Airport Data Management")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")
    selector = int(input("Please choose an option (1-3): "))
    if selector == 1:
        apid2 = str(input("Enter the ICAO code: "))
        apnm3 = str(input("Enter the airport name: "))
        airports.update(data_compiler(apid2,apnm3))
        print(f"Airport {apnm3} with ICAO code {apid2} has been added.")
        exit
    elif selector == 2:
        try:
            search = str(input("Enter the ICAO code: "))
            print(f"The airport with ICAO code {search} is {airports[search]}.")
            exit
        except:
            print(f"No airport found with ICAO code {search}.")
            exit
    elif selector == 3:
        print("Thank you for using the Airport Data Management system. Goodbye!")
        break


