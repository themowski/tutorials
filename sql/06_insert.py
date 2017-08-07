# There are two forms of INSERT. Call them "positional" and "keyword".
# Positional is:
#   INSERT INTO Track VALUES (column0value, column1value, ..., columnNvalue);
# Keyword is:
#   INSERT INTO Track (firstcolumnname, othercolumnname, othercolumnnameinanyorder, ...) VALUES (valueforfirstcolumnname, valueforothercolumnname, ...);

# Note that if we use positional we need to put a placeholder NULL for
#   the TrackId INTEGER PRIMARY KEY AUTOINCREMENT column.
# It is marked as NOT NULL -- PRIMARY KEYs cannot be NULL -- but the database
#   will populate the column for us, as described in the
#   create_table_primary_key module.

# The keyword form is generally preferred when there are more than 4-5 columns.
# In these situations you often have "sparse" tables, where most of the columns can
#   and will be NULL.
# Using the keyword forms allows you to only specify the columns that have values in
#   the row you're inserting.
# Everything else is implicitly NULL.

# Note that string literals are single-quoted like 'this'.
# If you need to put a single quote in a string literal, double the single quotes:
# 'this isn''t'


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
"""
INSERT INTO Track
    (Name, Composer, Milliseconds, Bytes, UnitPrice)
    VALUES ('''Round Midnight', 'Miles Davis', 357459, 11590284, 0.99);
"""
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
