season_nmbr = int(input("Enter the number of a month (1-12): "))
print(f"You entered: {season_nmbr}")
def get_season(a):
    if ( 0 < a < 13) == False:
        print("Please enter a number between 1 and 12.")
        return None
    elif (1 <= a <= 2) or a == 12:
        print("The season is winter.")
    elif 3 <= a <= 5:
        print("The season is spring.")
    elif 6 <= a <= 8:
        print("The season is summer.")
    elif 9 <= a <= 11:
        print("The season is autumn.")
get_season(season_nmbr)