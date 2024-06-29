import csv
with open("students_rec.csv","w",newline="") as file:
    empdata = csv.writer(file)
    empinfo=[['Empid','Name','Salary','Age'],
    [101,'John',5000,23],
    [102,'David',6000,47],
    [103,'Sara',8000,39],
    [104,'Roger',7000,42]
    ]
    empdata.writerows(empinfo)