#!/usr/bin/python3

import pandas as pd

"""
Create a Dataframe using pandas. You are going to create a
code to put the following into a Dataframe. You will use the
information in the table below. Basically, you are going to
recreate this table using pandas. Use the information in the table
to recreate the table.

year    Title       genre
===========================
2009    Brothers    Drama
2002    Spider-Man  Sci-fi
2009    WatchMen    Drama
2010    Inception   Sci-fi
2009    Avatar      Fantasy
"""


# Create a dictionary 'data' containing information about movies.
data = {
    "year": [2009, 2002, 2009, 2010, 2009],  # List of release years for the movies.
    "Title": [
        "Brothers",
        "Spider-Man",
        "WatchMen",
        "Inception",
        "Avatar",
    ],  # List of movie titles.
    "genre": ["Drama", "Sci-fi", "Drama", "Sci-fi", "Fantasy"],  # List of movie genres.
}

# Convert the 'data' dictionary into a pandas DataFrame.
movies_df = pd.DataFrame.from_dict(data)

print(movies_df)
