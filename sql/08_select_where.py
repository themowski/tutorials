# Usually we'd like to limit the rows we SELECT.
# To do this we add a WHERE clause to the end of the SELECT.
# SELECT <columns> FROM <table> WHERE <predicates>
# Predicates are boolean expressions with the usual operators:
#   =   (equal to)
#   <>  (not equal to)
#   <   (less than)
#   <=  (less than or equal to)
#   >   (greater than)
#   >=  (greater than or equal to)
#   AND, OR, NOT
#   IS NULL, IS NOT NULL
#   Plus a few less common operators like LIKE, IN, and BETWEEN ... AND.

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
"SELECT Name, UnitPrice FROM Track WHERE Name = 'Muffin Man';"
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
