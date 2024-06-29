import pickle
stu = {}
with open ('student_records .dat','wb') as input_file:
    ans = 'y'
    while ans.lower() == 'y':
        rno = int(input('enter your roll-number:- '))
        name = input('enter your name:- ')
        marks = float(input('enter your marks:- '))
        
        stu['RollNo']=rno
        stu['Name']=name
        stu['marks']=marks
        
        pickle.dump(stu,input_file)
        ans = input("want to enter more records? (y/n)...")
        