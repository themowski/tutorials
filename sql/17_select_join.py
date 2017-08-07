# When there is a relationship between the data in two (or more) tables
# we'll often want to get data from both tables at once.
# If we just SELECT the columns from the two tables we'll see the data
# in the order it was inserted in each table.
# What we really want is to see related columns.

# The JOIN below is an INNER JOIN. (The JOIN keyword by itself is an alias for INNER JOIN).
# This is the most common type of join, but there are many others:
# https://en.wikipedia.org/wiki/Join_%28SQL%29

# Note that the skeleton has changed to use the pre-populated chinook.sqlite
# database file.

SQL = ('''
SELECT
    Album.AlbumId, Album.Title, Track.TrackId, Track.Name, Track.AlbumId
FROM
    Album, Track
WHERE
    Album.AlbumId = 27
LIMIT 1
''',
'''
SELECT
    Album.AlbumId, Album.Title, Track.TrackId, Track.Name, Track.AlbumId
FROM
    Track JOIN Album
        ON Track.AlbumId = Album.AlbumId
WHERE
    Album.AlbumId = 27
LIMIT 10
''',
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
