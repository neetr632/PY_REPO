import csv
with open ("students_rec.csv") as input_file:
    empdata = csv.reader(input_file)
    for x in empdata:
        print(x)