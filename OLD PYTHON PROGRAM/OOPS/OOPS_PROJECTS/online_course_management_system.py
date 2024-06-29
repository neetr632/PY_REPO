import os

number_of_students = int(input("Enter the number of student details you want to enter: "))

class Courses:
    def __init__(self, Course_id, Course_name, Course_desc, file_path):
        self.Course_id = Course_id
        self.Course_name = Course_name
        self.Course_desc = Course_desc
        self.students_List = []
        self.file_path = file_path
        self.load_from_file()

    def add_student(self, number_of_students):
        for i in range(number_of_students):
            print(f"\nEnter Details For The Student {i+1}:")
            student_info = {
                "STUDENT ID": int(input("Enter the student ID of 3 digits: ")),
                "NAME": input("Enter the NAME for the student: "),
                "AGE": int(input("Enter the student AGE: ")),
                "GRADE": input("Enter the student GRADE: "),
                "COURSE NAME": self.Course_name,
                "COURSE ID": self.Course_id,
                "COURSE DESC": self.Course_desc
            }
            self.students_List.append(student_info)

    def write_students_details(self):
        with open(self.file_path, "w") as f:
            for student_info in self.students_List:
                f.write(f"STUDENT ID: {student_info.get('STUDENT ID', 'N/A')}\n")
                f.write(f"NAME: {student_info.get('NAME', 'N/A')}\n")
                f.write(f"AGE: {student_info.get('AGE', 'N/A')}\n")
                f.write(f"GRADE: {student_info.get('GRADE', 'N/A')}\n")
                f.write(f"COURSE NAME: {student_info.get('COURSE NAME', 'N/A')}\n")
                f.write(f"COURSE ID: {student_info.get('COURSE ID', 'N/A')}\n")
                f.write(f"COURSE DESC: {student_info.get('COURSE DESC', 'N/A')}\n\n")

    def print_stu_details(self):
        print("ALL STUDENTS DETAILS PRESENT IN THE SYSTEM:")
        for student in self.students_List:
            print(student)

    def load_from_file(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                student_info = {}
                for line in f:
                    if line.strip():
                        key, value = line.split(": ")
                        student_info[key.strip()] = value.strip()
                    else:
                        if student_info:
                            self.students_List.append(student_info)
                            student_info = {}
                if student_info:
                    self.students_List.append(student_info)
        else:
            print("Previous Records Do Not Exist...")

    def delete_student(self):
        delete_ID = input("Enter the student ID that you want to delete: ")
        for student_info in self.students_List:
            if student_info["STUDENT ID"] == delete_ID:
                print("Student details to be deleted: ", student_info)
                confirm_delete = input("Are you sure..? Enter Yes to Delete: ")
                if confirm_delete.lower() == "yes":
                    self.students_List.remove(student_info)
                    print("Student Details Deleted Successfully.")
                else:
                    print("Student Details Not Deleted.")
                break
        else:
            print("Student ID Not Found", delete_ID)

course_details = Courses("C101", "Python Programming", "Learn Python from scratch", "student_list.txt")
# course_details.add_student(number_of_students=number_of_students)
course_details.print_stu_details()
course_details.delete_student()
course_details.write_students_details()
course_details.print_stu_details()

