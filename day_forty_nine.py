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
                     """CREATE TABLE if not exists movies (
                                             id integer primary key,
                                             year integer,
                                             title text,
                                             genre text)"""
                     )
        curr.execute("""
                     insert into movies (year, Title, genre)
                     values (2009, 'Brothers', 'Drama'),
                     (2002, 'Spider Man', 'Sci-fi'),
                     (2009,'WatchMen','Drama'),
                     (2010,'Inception','Sci-fi'),
                     (2009,'Avatar','Fantasy');
                     """)

        df = pd.read_sql_query('select * from movies', conn, index_col='id')
        print(f'{df}\n\n')
        df = pd.read_sql_query("""
                          select *
                          from movies
                          where Title = 'Brothers'
                          """, conn, index_col='id')
        print(f'{df}\n\n')
        df = pd.read_sql_query('select * from movies where year = 2009',
                               conn, index_col='id')
        print(f'{df}\n\n')
        df = pd.read_sql_query("""select *
                                 from movies
                                 where genre = 'Fantasy' or genre = 'Drama'
                                 """, conn, index_col='id')
        print(f'{df}\n\n')
        curr.execute('drop table movies')
        # curr.execute('select * from movies')
        # result = curr.fetchall()
        # for row in result:
        #     print(row)

        # curr.execute("""select *
        #              from movies
        #              where title = 'Brothers'
        #              """)
        # result = curr.fetchall()
        # for row in result:
        #     print(row)

        # curr.execute("""select *
        #              from movies
        #              where year = 2009
        #              """)
        # result = curr.fetchall()
        # for row in result:
        #     print(row)

        # curr.execute("""select *
        #              from movies
        #              where genre = 'Fantasy' or 'Drama'
        #              """)

        # for row in result:
        #     print(row)


print(make_movie_db())
