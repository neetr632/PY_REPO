if __name__ == "__main__":
    students = []

    # Collect input data
    for _ in range(int(input().strip())):
        name = input().strip()
        grade = float(input().strip())
        students.append([name, grade])

    # Extract unique grades and sort them
    grades = sorted(set(student[1] for student in students))

    # Find the second lowest grade
    second_lowest_grade = grades[1]

    # Find the students with the second lowest grade
    second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]

    # Sort students' names alphabetically
    second_lowest_students.sort()

    # Print each name on a new line
    for student in second_lowest_students:
        print(student)
