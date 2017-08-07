# Occasionally it is important that multiple updates (INSERTs, DELETEs, UPDATEs)
# are applied atomically, so that we know they were either all applied properly or
# none of them were.

# The classic example is a bank customer transferring money between two accounts.
# The debit to one account and the credit to the other account must be applied
# together, as an atomic unit. Otherwise we might have a situation where the
# debit is correctly applied but the credit fails ("losing" the customer's money)
# or vice versa (giving the customer too much money), depending on the order of
# the operations.


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

        cur.execute('BEGIN TRANSACTION;')
        insert_sql = 'INSERT INTO Regents VALUES (NULL, ?, ?, ?, ?, ?);'
        with open('regents.csv') as f:
            for row_i, row in enumerate(csv.reader(f)):
                if row_i == 0:
                    continue
                # Use the form cur.execute(sql str, parameters list or tuple)
                # to do proper escaping as well as reuse the SQL string.
                print 'Executing', insert_sql, 'with', row
                cur.execute(insert_sql, row)
        # If we don't reach this point because of an error,
        # the database will roll back the transaction, restoring
        # the state of the database to what it was before the
        # BEGIN TRANSACTION was executed.
        conn.commit()
        # Will also commit() on close

        print 'SELECTing all rows'
        for row in cur.execute('SELECT * FROM Regents;'):
            print row
    finally:
        cur.close()
finally:
    conn.close()
