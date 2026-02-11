import mysql.connector

link = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='Spizium',
    password='Opgekonkerd',
    autocommit=True,
    collation='utf8mb3_general_ci',
    )

def portfetch(id):

    sql = f"SELECT Name, Municipality FROM airport WHERE Ident='{id.upper()}'"
    cursor = link.cursor()
    cursor.execute(sql)
    tulos = cursor.fetchall()
    check = cursor.rowcount #Tarkistaa onko palautettu mitään!
    if check == 0:
        return False
    else:
        return tulos

yeet = input("Enter the ICAO code of an airport: ")
FUCK = portfetch(yeet)
if FUCK != False:
    print(f"Airport name: {FUCK[0][0]}")
    print(f"Location: {FUCK[0][1]}")
else:
    print(f"No airport found with ICAO code {yeet.upper()}")