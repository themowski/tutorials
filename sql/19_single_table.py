# Create a single table to hold the rows of the CSV.

import csv
import sqlite3

conn = sqlite3.connect(':memory:')
try:
    try:
        cur = conn.cursor()

        cur.execute('''
CREATE TABLE Salary (
    Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Department VARCHAR NOT NULL,
    AgencyInstitution VARCHAR,
    Name VARCHAR NOT NULL,
    Gender CHAR(1) NOT NULL,
    PlaceOfResidence VARCHAR,
    Position VARCHAR NOT NULL,
    SalaryJuly2013 NUMERIC,
    TotalFY2013Salary NUMERIC NOT NULL,
    TravelAndSubsistence NUMERIC NOT NULL
);''')

        with open('salaries.csv') as f:
            for row_i, row in enumerate(csv.reader(f)):
                if row_i == 0:
                    continue
                insert_sql = 'INSERT INTO Salary VALUES (NULL' + (', ?' * len(row)) + ');'
                if row_i < 10:
                    print insert_sql
                values = []
                for column in row:
                    if len(column) > 0:
                        values.append(column)
                    else:
                        values.append(None) # NULL
                if row_i < 10:
                    print values
                cur.execute(insert_sql, values)
    finally:
        cur.close()
finally:
    conn.close()
