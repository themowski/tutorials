import csv
import sqlite3

SQL = (
'SELECT * FROM Salary LIMIT 5',
'''
SELECT
    Salary.Name, Department.Name, Position.Name, Salary.TotalFY2013Salary
FROM
    Salary JOIN Department ON Salary.DepartmentId = Department.Id
           JOIN Position ON Salary.PositionId = Position.Id
ORDER BY
    Salary.TotalFY2013Salary DESC
LIMIT 10;
''',
'''
SELECT
    Salary.DepartmentId, SUM(Salary.TotalFY2013Salary)
FROM
    Salary
GROUP BY
    Salary.DepartmentId
''',
'''
SELECT
    Department.Id, Department.Name, AVG(TotalFY2013Salary)
FROM
    Salary JOIN Department ON Salary.DepartmentId = Department.Id
GROUP BY
    Salary.DepartmentId
ORDER BY
    AVG(TotalFY2013Salary) DESC
''',
'''
SELECT
    Position.Name, SUM(TotalFY2013Salary)
FROM
    Salary JOIN Position ON Salary.PositionId = Position.Id
GROUP BY
    Salary.PositionId
ORDER BY
    SUM(TotalFY2013Salary) DESC
LIMIT 10
''',
'''
SELECT
    Position.Name, COUNT(*)
FROM
    Salary JOIN Position ON Salary.PositionId = Position.Id
GROUP BY Salary.PositionId
ORDER BY COUNT(*) DESC
LIMIT 10
'''
)

conn = sqlite3.connect('salaries.sqlite')
try:
    try:
        cur = conn.cursor()

        for sql in SQL:
            print 'Executing', sql.strip()
            for row in cur.execute(sql):
                print row
            print
    finally:
        cur.close()
finally:
    conn.close()
