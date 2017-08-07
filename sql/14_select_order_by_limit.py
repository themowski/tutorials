# We can also reorder and/or limit the amount of data that is returned.

# Note that the relational database does not guarantee that rows will be
#   returned in a specific order unless you specify one using ORDER BY.
# In the absence of ORDER BY the database will usually return rows in
# insertion order, which is also the order of an AUTOINCREMENT INTEGER PRIMARY KEY.

SQL = (
'SELECT * FROM Track LIMIT 1', # Only return one row, the "first" in the default ordering
'SELECT * FROM Track LIMIT 2 OFFSET 2', # Return two rows starting from what would have been the third row (0-based indexing)
'SELECT * FROM Track ORDER BY UnitPrice LIMIT 2', # First n tracks ordered by unit price, ascending i.e. the "least expensive n"
'SELECT * FROM Track ORDER BY UnitPrice ASC LIMIT 2', # Same - the ASC keyword is implicit above
'SELECT * FROM Track ORDER BY UnitPrice DESC LIMIT 2', # Unit price descending order i.e. the "most expensive n"
'SELECT Name, AlbumId, UnitPrice FROM Track ORDER BY UnitPrice DESC, AlbumId ASC LIMIT 10',
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
