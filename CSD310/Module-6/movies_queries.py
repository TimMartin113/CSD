import mysql.connector
from mysql.connector import errorcode

from dotenv import dotenv_values

# load secrets
secrets = dotenv_values(".env")


config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    print(
        "\nDatabase user {} connected to MySQL on host {} with database {}".format(
            config["user"],
            config["host"],
            config["database"]
        )
    )

    input("\nPress Enter to continue...")

# Display Studio records

    print("\n-- DISPLAYING Studio RECORDS --")

    cursor.execute("SELECT studio_id, studio_name FROM studio")

    for studio in cursor.fetchall():

        print("Studio ID: {}".format(studio[0]))

        print("Studio Name: {}\n".format(studio[1]))

    # Display Genre records

    print("-- DISPLAYING Genre RECORDS --")

    cursor.execute("SELECT genre_id, genre_name FROM genre")

    for genre in cursor.fetchall():

        print("Genre ID: {}".format(genre[0]))

        print("Genre Name: {}\n".format(genre[1]))

    # Display Short Film records

    print("-- DISPLAYING Short Film RECORDS --")

    cursor.execute("""

        SELECT film_name, runtime

        FROM film

        WHERE runtime < 120

    """)

    for film in cursor.fetchall():

        print("Film Name: {}".format(film[0]))

        print("Runtime: {}\n".format(film[1]))

    # Display Director records

    print("-- DISPLAYING Director RECORDS in Order --")

    cursor.execute("""

        SELECT film_name, director

        FROM film

        ORDER BY director

    """)

    for movie in cursor.fetchall():

        print("Film Name: {}".format(movie[0]))

        print("Director: {}\n".format(movie[1]))

except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)

finally:

    if 'cursor' in locals():
        cursor.close()

    if 'db' in locals() and db.is_connected():
        db.close()