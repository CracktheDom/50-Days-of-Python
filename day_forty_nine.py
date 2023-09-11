#!/usr/bin/python3

import sqlite3
import pandas as pd

"""
For this challenge, you are going to create a database using
Python’s SQLite. You will import SQLite into your script.
Create a database called movies.db. In that database, you are
going to create a table called movies. In that table, you are
going to save the following movies:
year        title           genre
2009        Brothers        Drama
2002        Spider Man      Sci-fi
2009        WatchMen        Drama
2010        Inception       Sci-fi
2009        Avatar          Fantasy

a) Once you create a table, run a SQL query to see all the
movies in your table.
b) Run another SQL query to select only the movie Brothers
from the list.
c) Run another SQL query to select all movies that were
released in 2009 from your table.
d) Run another query to select movies in the fantasy and
drama genre.
e) Run a query to delete all the contents of your table
"""


def make_movie_db():
    with sqlite3.connect("./movies.db") as conn:
        curr = conn.cursor()
        curr.execute(
            """CREATE TABLE IF NOT EXISTS movies (
            id integer primary key,
            year integer,
            title text,
            genre text)"""
        )
        curr.execute(
            """INSERT INTO movies (year, Title, genre)
             values (2009, 'Brothers', 'Drama'),
            (2002, 'Spider Man', 'Sci-fi'),
            (2009,'WatchMen','Drama'),
            (2010,'Inception','Sci-fi'),
            (2009,'Avatar','Fantasy');
            """
        )

        movies_df = pd.read_sql_query("SELECT * FROM movies", conn, index_col="id")
        print(f"{movies_df}\n\n")
        brothers_movies = pd.read_sql_query(
            """
            SELECT *
            FROM movies
            WHERE Title = 'Brothers'
            """,
            conn,
            index_col="id",
        )
        print(f"{brothers_movies}\n\n")
        movies_2009 = pd.read_sql_query(
            """SELECT * FROM movies WHERE year = 2009""",
            conn,
            index_col="id",
        )
        print(f"{movies_2009}\n\n")
        fantasy_drama = pd.read_sql_query(
            """SELECT * FROM movies
            WHERE genre = 'Fantasy' or genre = 'Drama' """,
            conn,
            index_col="id",
        )
        print(f"{fantasy_drama}\n\n")
        curr.execute("DROP TABLE movies")


if __name__ == "__main__":
    print(make_movie_db())
