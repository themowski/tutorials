# Create a table to describe media tracks
# The basic syntax of CREATE TABLE is
#   CREATE TABLE TableName (firstColumnName TYPE, secondColumnName TYPE, ...);

# SQL keywords like CREATE TABLE and the types (VARCHAR, etc.) are case-insensitive.
# Column names are usually case-sensitive, though this differs between database
#   products (MySQL, SQL Server, SQLite, et al.) and configurations. You should always
#   assume that column names are case sensitivity.
# Some people prefer CamelCaseColumnNames. Others like underscore_separated_names.
# Choose a style that looks good to you and be consistent.

# Whitespace (spaces, tabs, newlines) is ignored in this context,
#   so you can format for readability.

# A few column types are used here:
#   VARCHAR = variable number of characters (like a Python string)
#   INTEGER = variable-width integer (no real numbers)
#   NUMERIC = arbitrary-precision real/decimal number, used for currency values

SQL = ('''
CREATE TABLE Track
(
    Name VARCHAR,
    Composer VARCHAR,
    Milliseconds INTEGER,
    Bytes INTEGER,
    UnitPrice NUMERIC
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
