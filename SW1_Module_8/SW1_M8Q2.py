import mysql.connector

def get_airports_by_country(country_code):
    link = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='Spizium',
        password='Opgekonkerd',
        autocommit=True,
        collation='utf8mb3_general_ci',
    )
    poopql = f"SELECT type, COUNT(*) AS COUNT from airport WHERE iso_country = '{country_code}' group by type;"
    cursor = link.cursor()
    cursor.execute(poopql)
    poopql_output = cursor.fetchall()
    return poopql_output

def run_country_program(a):
    aplist = get_airports_by_country(a)
    print(f"Airports in {idinput}: ")
    for i in aplist:
        for j in reversed(i):
            print(j, end=' ')
        print("airports")

idinput = input("Enter the country code (e.g., FI for Finland): ")
run_country_program(idinput)
