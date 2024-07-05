if __name__ == "__main__":
    students = []
for _ in range(int(input())):
    name = str(input())
    try:
        score = input()
        if "." in score:
            score = float(score)
        else:
            score = int(score)
        students.append([name, score])
    except ValueError:
        print("Invalid input! Please enter a valid number for score.")

sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
marks = [student[1] for student in students if student[1] > 0]
marks.sort()
if len(marks) > 1:
    repeated_marks = []
    for i in marks:
        if i == marks[1]:
            repeated_marks.append(i)
    names = [
        students[i][0] for i in range(len(students)) if students[i][1] in repeated_marks
    ]
    names.sort()
    for i in names:
        print(i)
else:
    for x in students:
        if x[1] in marks:
            print(x[0])
            
