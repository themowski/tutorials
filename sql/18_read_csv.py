# Look at the contents of the salaries.csv file to get some idea how to
# model it in tables.

import csv

with open('salaries.csv') as f:
    for row_i, row in enumerate(csv.reader(f)):
        print row
        if row_i >= 5:
            break
