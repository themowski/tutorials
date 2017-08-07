SQL = ('''
SELECT * FROM sqlite_master;
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
