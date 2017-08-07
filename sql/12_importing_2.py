# http://xkcd.com/327/

import csv
import sqlite3

conn = sqlite3.connect(':memory:')
try:
    try:
        cur = conn.cursor()

        cur.execute('''
CREATE TABLE Regents (
    Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Year VARCHAR NOT NULL,
    UniversityName VARCHAR NOT NULL,
    StudentClassification VARCHAR NOT NULL,
    ResidentStatus VARCHAR NOT NULL,
    Headcount INTEGER NOT NULL
);''')

        insert_sql = 'INSERT INTO Regents VALUES (NULL, ?, ?, ?, ?, ?);'
        with open('regents.csv') as f:
            for row_i, row in enumerate(csv.reader(f)):
                if row_i == 0:
                    continue
                # Use the form cur.execute(sql str, parameters list or tuple)
                # to do proper escaping as well as reuse the SQL string.
                print 'Executing', insert_sql, 'with', row
                cur.execute(insert_sql, row)

        # Could also use executemany:
        #with open('regents.csv') as f:
        #    cur.executemany(insert_sql, [row for row_i, row in enumerate(csv.reader(f)) if row_i != 0])

        print 'SELECTing all rows'
        for row in cur.execute('SELECT * FROM Regents;'):
            print row
    finally:
        cur.close()
finally:
    conn.close()
