# There are many different ways to query (SELECT) rows from a table.
# Here we will SELECT all of the rows in the table, using the simple form
# SELECT <comma-separated list of columns> FROM <table>
# <columns> can also be *, meaning all columns
# SELECT * FROM Track means "select all rows from the table Track"

SQL = ('''
CREATE TABLE Track
(
    TrackId INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Name VARCHAR(200) NOT NULL,
    Composer VARCHAR(220),
    Milliseconds INTEGER NOT NULL,
    Bytes INTEGER,
    UnitPrice NUMERIC(10, 2) NOT NULL
);
''',
'''
INSERT INTO Track
    VALUES (NULL, 'Mas Que Nada', 'Jorge Ben', 248398, 8255254, 0.99);
''',
'''
INSERT INTO Track
    (Name, Composer, Milliseconds, Bytes, UnitPrice)
    VALUES ('Muffin Man', 'Frank Zappa', 332878, 10891682, 0.99);
''',
'SELECT Name FROM Track;',
'SELECT * FROM Track;'
)

import sqlite3
conn = sqlite3.connect(':memory:')
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
