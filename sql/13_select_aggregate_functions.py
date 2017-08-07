# We can refine SELECT to manipulate and/or filter the data
# before it is returned to our program. The goal is to do as much
# work as possible as close to the database as possible.

SQL = (
'SELECT MIN(Bytes) FROM Track',
'SELECT MAX(Bytes) FROM Track',
'SELECT SUM(Bytes) FROM Track',
'SELECT AVG(Bytes) FROM Track',
'SELECT COUNT(UnitPrice) FROM Track', # Number of non-NULL values
'SELECT COUNT(*) FROM Track', # Number of rows in the table
'SELECT DISTINCT UnitPrice FROM Track', # Distinct values
)

import sqlite3
conn = sqlite3.connect('chinook.sqlite')
try:
    cur = conn.cursor()
    try:
        for sql in SQL:
            print 'Executing', sql.strip()
            for row in cur.execute(sql):
                print row
            print
    finally:
        cur.close()
finally:
    conn.close()
