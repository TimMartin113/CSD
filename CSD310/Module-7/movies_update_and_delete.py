"""
Title: movies_update_and_delete.py
Author: Timothy Martin
Course: CSD-310 Database Development and Use
Module: 7 - Movies Management
Date: July 8, 2026
Description:
This program connects to a MySQL database named "movies" using credentials
stored in a .env file. It displays movie information using INNER JOINs,
inserts a new movie record, updates an existing movie record, and deletes
a movie record.
"""


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


def show_films(cursor, title):
    """
    Executes an INNER JOIN query to display film information
    including genre and studio names.
    """

    cursor.execute("""
        SELECT
            film_name AS Name,
            film_director AS Director,
            genre_name AS Genre,
            studio_name AS Studio
        FROM film
        INNER JOIN genre
            ON film.genre_id = genre.genre_id
        INNER JOIN studio
            ON film.studio_id = studio.studio_id;
    """)

    films = cursor.fetchall()

    print("\n-- {} --".format(title))

    for film in films:
        print("Film Name: {}".format(film[0]))
        print("Director: {}".format(film[1]))
        print("Genre Name ID: {}".format(film[2]))
        print("Studio Name: {}\n".format(film[3]))


try:

    # connect to database
    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    print(
        "\nDatabase user {} connected to MySQL on host {} with database {}".format(
            config["user"],
            config["host"],
            config["database"]
        )
    )


    # display original movie list
    show_films(cursor, "DISPLAYING FILMS")


    # ----------------------------------------------------
    # Insert a new movie
    # ----------------------------------------------------
    cursor.execute("""
        INSERT INTO film
        (
            film_name,
            film_releaseDate,
            film_runtime,
            film_director,
            studio_id,
            genre_id
        )
        VALUES
        (
            'The Matrix',
            1999,
            136,
            'The Wachowskis',
            1,
            2
        );
    """)

    db.commit()

    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")


    # ----------------------------------------------------
    # Update Alien from SciFi to Horror
    # ----------------------------------------------------
    cursor.execute("""
        UPDATE film
        SET genre_id =
        (
            SELECT genre_id
            FROM genre
            WHERE genre_name = 'Horror'
        )
        WHERE film_name = 'Alien';
    """)

    db.commit()

    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror")


    # ----------------------------------------------------
    # Delete Gladiator
    # ----------------------------------------------------
    cursor.execute("""
        DELETE FROM film
        WHERE film_name = 'Gladiator';
    """)

    db.commit()

    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")


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