# Values in a relational database should be atomic, for ease of querying,
# performance, constraint enforcement, avoiding duplication, and other
# reasons.
# This is called the "first normal form" or 1NF.

# We often want to describe "has-a" relationships between entities in
# our data model, however. An album "has-a" track, a genre, and an artist,
# all of which are entities in their own right, with their own sets of
# attributes (columns).

# More generally, we want to describe n-to-1 and n-to-m relationships.
# In the former case we'll specify the relationship's inverse:
# n tracks belong to 1 album; n albums belong to 1 genre; and so on.
# Thus, instead of album having n "pointers" to all of its tracks,
# each track has one pointer to its album. This single pointer is a foreign
# key:
# CREATE TABLE Track (
#     ...
#     FOREIGN KEY (AlbumId) REFERENCES Album (AlbumId)
# );
# The FOREIGN KEY is a constraint:
# When we insert rows into the Track table we must specify an AlbumId column
# that corresponds to one in the Album table. (By convention the foreign
# key column in Track has the same name as the primary key in Album it points
# to.)

# How would you specify n-to-m relationships in SQL?

SQL = ('''
CREATE TABLE Album
(
    AlbumId INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Title VARCHAR(160)  NOT NULL
);
''',
'''
CREATE TABLE Track
(
    TrackId INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Name VARCHAR(200)  NOT NULL,
    AlbumId INTEGER,
    MediaTypeId INTEGER  NOT NULL,
    GenreId INTEGER,
    Composer VARCHAR(220),
    Milliseconds INTEGER  NOT NULL,
    Bytes INTEGER,
    UnitPrice NUMERIC(10,2)  NOT NULL,
    FOREIGN KEY (AlbumId) REFERENCES Album (AlbumId)
);
''',
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
