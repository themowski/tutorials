# We may want to be more specific about the ranges of values a column can hold,
# in order to reject values that are too long when someone tries to insert them
# into the database.
# The goal is to constrain the column values as much as possible so you can make
# some assumptions about the form of the data.

# Name can hold up to 200 characters
# Composer can hold up to 220
# Unit price can have at most 10 digits to the left of the decimal point
#   and at most two digits to the right.

SQL = ('''
CREATE TABLE Track
(
    Name VARCHAR(200) NOT NULL,
    Composer VARCHAR(220),
    Milliseconds INTEGER NOT NULL,
    Bytes INTEGER,
    UnitPrice NUMERIC(10, 2) NOT NULL
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
