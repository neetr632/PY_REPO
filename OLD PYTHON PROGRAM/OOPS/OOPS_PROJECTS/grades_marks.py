from random import randint
from faker import Faker
import openpyxl

f = Faker()
def generate_fake_name():
    return f.name()

list_of_name = [generate_fake_name() for _ in range(10)]
with open("names.txt", 'w') as f:
    for name in list_of_name:
        f.write(name + '\n')
    
marks = [randint(1,100) for _ in range(10)]  
with open("marks.txt", 'w') as f:
    for mark in marks:
        f.write(str(mark) + '\n')
average = sum(marks)/len(marks)
print(f"the average of the marks is: {average}")
record = dict(zip(list_of_name, marks))

# Create a new Excel workbook and select the active worksheet
workbook = openpyxl.Workbook()
xlsx = workbook.active

# Write the header row
xlsx.append(["Name", "Marks"])

# Write data from the dictionary to the worksheet
for name, marks in record.items():
    xlsx.append([name, marks])

# Save the workbook
workbook.save("records.xlsx")

