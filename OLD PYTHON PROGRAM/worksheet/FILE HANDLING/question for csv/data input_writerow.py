import csv

with open("sample.csv", "w", newline="") as file:
    empdata = csv.writer(file)
    empdata.writerow(['empid','name','salary'])
    num_employees = 0
    for i in range(5):
        print("Employee Record",i+1,":")
        empid=int(input("enter your employee id :"))
        empname=input(f"Enter the Name of employee having id:-{empid} :-")
        empsalary=int(input(f"Enter {empname}'s Salary:"))
        exit_input=input("Do you want to exit ? Enter Y or N :->")
        emprec=[empid,empname,empsalary]
        empdata.writerow(emprec)
        num_employees +=1
        if exit_input.lower() in ("y", "Y"):
            break
print(f"the CSV file has total of {num_employees} employees registered.")