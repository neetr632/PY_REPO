import pickle

student_1 = {'name': 'Alice', 'age': 25, 'subjects': ['Math', 'Physics']}
student_2 = {'name': 'BOB', 'age': 22, 'subjects': ['Math', 'Physics']}


with open("students.dat", "wb") as output_file:
    pickle.dump(student_1, output_file)
    pickle.dump(student_2, output_file)
    output_file.flush()
    print("Data Inserted Successfully")
