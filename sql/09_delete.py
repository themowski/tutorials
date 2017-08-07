# The DELETE (rows) operation has a similar form to SELECT, namely
# DELETE FROM <table> [WHERE predicates]
# If you don't specify a WHERE clause it will delete all rows.

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
'SELECT * FROM Track;',
"DELETE FROM Track WHERE Name = 'Muffin Man';",
'SELECT * FROM Track;',
'DELETE FROM Track;',
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
