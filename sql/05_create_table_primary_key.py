# Every row in the table should have a column that uniquely identifies the row,
#   mostly for performance reasons (locating a single row quickly).
# This column is called the primary key. It is usually an INTEGER,
#   though it doesn't have to be.

# When we insert rows into the table we are responsible for ensuring the values
#   in this column are unique.
# When the data itself has a unique column, this is obvious,
#   but for many tables there is no obvious unique identifier.
# Tracks can be identified by name, but their names are unlikely to be unique.
# In this case we create a special column, by convention called "id" or
#   **TABLENAME**Id (here TrackId).

# Then we have the problem of how to populate this column when we're inserting rows.
# Every "id" needs to be unique, but we don't know which "id" values have been
#   used already unless we look at the existing rows' "id" columns.
# We would have to scan the table to see what values (primary keys) were already
# there, then pick the "next" one.
# If multiple users were writing to the table concurrently there's a strong
#   possibility that they will both scan and pick the same "id", in which case
#   one of the user's insertions will fail.

# Databases address this situation by allowing you to mark the PRIMARY KEY
#   column as AUTOINCREMENT, meaning "use the next unique integer value
#   when I insert a row".
# We don't have to include this column in our inserted values,
#   because it will be populated automatically.

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
