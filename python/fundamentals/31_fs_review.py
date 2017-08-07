import csv

# Thus far we've only read files from the current directory:
with open('regents.csv') as f:
    for line in f.readlines():
        pass
    # implicit f.close() here

# Alternatively:
f = open('regents.csv')
try:
    for line in f.readlines():
        pass
finally:
    f.close()

# We've used the csv library to parse the lines as we read them:
with open('regents.csv') as f:
    for row in csv.reader(f):
        pass
