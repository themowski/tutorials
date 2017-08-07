# Import data from a CSV file into a SQLite table
# This is in Python, but should be straightforward to translate to other languages.

import csv
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect(':memory:')
try:
    try:
        # Get a cursor on the database in order to execute SQL statements
        cur = conn.cursor()

        # Create a table schema for this data
        cur.execute('''
CREATE TABLE Regents (
    Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Year VARCHAR NOT NULL,
    UniversityName VARCHAR NOT NULL,
    StudentClassification VARCHAR NOT NULL,
    ResidentStatus VARCHAR NOT NULL,
    Headcount INTEGER NOT NULL
);''')

        # Open the CSV file
        with open('regents.csv') as f:
            # Loop over the rows in the CSV file
            # row_i=0, row=<row 0 i.e. the first row in the file>
            # row_i=1, row=<row 1>
            # etc.
            for row_i, row in enumerate(csv.reader(f)):
                if row_i == 0:
                    # Skip the header row
                    # Could also use headers to form the CREATE TABLE
                    continue

                # Create an INSERT statement by concatenating values from the CSV row
                insert = 'INSERT INTO Regents VALUES (NULL' # NULL is for the Id
                for column in row:
                    insert += ', ' + "'" + column + "'"
                insert += ');'
                print 'Executing', insert
                # Database will convert 'headcount' to an INTEGER for us
                cur.execute(insert)

        print 'SELECTing all rows'
        for row in cur.execute('SELECT * FROM Regents;'):
            print row
    finally:
        cur.close()
finally:
    conn.close()
