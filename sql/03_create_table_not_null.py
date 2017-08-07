# Some of the columns must have values i.e., they can not be NULL

SQL = ('''
CREATE TABLE Track
(
    Name VARCHAR NOT NULL,
    Composer VARCHAR,
    Milliseconds INTEGER NOT NULL,
    Bytes INTEGER,
    UnitPrice NUMERIC NOT NULL
);
''',)

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
