# Create different tables for categorical columns.
# This is likely what the/a source relational database for the CSV looks like.

import csv
import sqlite3

conn = sqlite3.connect('salaries.sqlite')
try:
    try:
        cur = conn.cursor()

        for drop_table_sql in (
'DROP TABLE IF EXISTS Department;',
'DROP TABLE IF EXISTS AgencyInstitution;',
'DROP TABLE IF EXISTS PlaceOfResidence;',
'DROP TABLE IF EXISTS Position;',
'DROP TABLE IF EXISTS Salary;',
        ):
            cur.execute(drop_table_sql)

        for create_table_sql in (
'''
CREATE TABLE Department (
    Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Name VARCHAR NOT NULL
);''',
'''
CREATE TABLE AgencyInstitution (
    Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Name VARCHAR NOT NULL
);
''',
'''
CREATE TABLE PlaceOfResidence (
    Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Name VARCHAR NOT NULL
);
''',
'''
CREATE TABLE Position (
    Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Name VARCHAR NOT NULL
);
''',
'''
CREATE TABLE Salary (
    Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    DepartmentId INTEGER NOT NULL,
    AgencyInstitutionId INTEGER,
    Name VARCHAR NOT NULL,
    Gender CHAR(1) NOT NULL,
    PlaceOfResidenceId INTEGER,
    PositionId INTEGER NOT NULL,
    SalaryJuly2013 NUMERIC,
    TotalFY2013Salary NUMERIC NOT NULL,
    TravelAndSubsistence NUMERIC NOT NULL,
    FOREIGN KEY (DepartmentId) REFERENCES Department (Id),
    FOREIGN KEY (AgencyInstitutionId) REFERENCES AgencyInstitution (Id),
    FOREIGN KEY (PlaceOfResidenceId) REFERENCES PlaceOfResidence (Id),
    FOREIGN KEY (PositionId) REFERENCES Position (Id)
);'''):
            cur.execute(create_table_sql)

        with open('salaries.csv') as f:
            csv_rows = list(csv.reader(f))
        csv_rows.pop(0) # Ignore the header

        department_ids = {}
        agency_institution_ids = {}
        place_of_residence_ids = {}
        position_ids = {}
        for csv_row in csv_rows:
            department = csv_row[0]
            agency_institution = csv_row[1]
            place_of_residence = csv_row[4]
            position = csv_row[5]

            department_ids.setdefault(department, None)
            if len(agency_institution) > 0:
                agency_institution_ids.setdefault(agency_institution, None)
            if len(place_of_residence) > 0:
                place_of_residence_ids.setdefault(place_of_residence, None)
            position_ids.setdefault(position, None)
        print 'Department ids', department_ids

        for (table_name, ids) in (
            ('Department', department_ids),
            ('AgencyInstitution', agency_institution_ids),
            ('PlaceOfResidence', place_of_residence_ids),
            ('Position', position_ids),
        ):
            insert_sql = 'INSERT INTO ' + table_name + ' VALUES (NULL, ?);'
            for value in ids.keys():
                cur.execute(insert_sql, (value,))
                #if table_name == 'Department':
                #    print insert_sql, value, cur.lastrowid
                ids[value] = cur.lastrowid
            print table_name, ids
            conn.commit()

        insert_sql = 'INSERT INTO Salary VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?);'
        for csv_row_i, csv_row in enumerate(csv_rows):
            department, agency_institution, name, gender, place_of_residence, position, salary_july_2013, total_fy13_salary, travel_and_subsistence = csv_row
            department_id = department_ids[department]
            if len(agency_institution) > 0:
                agency_institution_id = agency_institution_ids[agency_institution]
            else:
                agency_institution_id = None
            if len(place_of_residence) > 0:
                place_of_residence_id = place_of_residence_ids[place_of_residence]
            else:
                place_of_residence_id = None
            position_id = position_ids[position]
            if len(salary_july_2013) == 0:
                salary_july_2013 = None
            values = (department_id, agency_institution_id, name, gender, place_of_residence_id, position_id, salary_july_2013, total_fy13_salary, travel_and_subsistence)
            if csv_row_i < 10:
                print values
            cur.execute(insert_sql, values)
        conn.commit()
    finally:
        cur.close()
finally:
    conn.close()
