import mysql.connector
from geopy import distance

def get_airport_coordinates(icao_code):
    link = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='Spizium',
        password='Opgekonkerd',
        autocommit=True,
        collation='utf8mb3_general_ci',
    )
    poopql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao_code}'"
    cursor = link.cursor()
    cursor.execute(poopql)
    poopql_output = cursor.fetchall()
    return poopql_output

def run_airport_distance(ap1, ap2):
    cord1 = get_airport_coordinates(ap1)
    cord1 = cord1[0]
    cord2 = get_airport_coordinates(ap2)
    cord2 = cord2[0]
    travel = (distance.distance(cord1, cord2).km)
    print(f"Distance between {ap1} and {ap2}: {round(travel, 2)} kilometers")

ap1 = input("Enter the ICAO code of the first airport: ")
ap2 = input("Enter the ICAO code of the second airport: ")
run_airport_distance(ap1, ap2)

