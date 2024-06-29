class onlinecourse:
    def __init__(self,course,instructor):
        self.course = course
        self.instructor = instructor
        self.students = []
        
#enroll students

    def enroll_students(self,name):
        self.students.append(name)
        print(f"{name} has been enrolled in '{self.course}' course.")
        
    def course_details(self):
        print(f"course: {self.course}")
        print(f"instructor name: {self.instructor}")
        print(f"Enrolled students: {',' .join(self.students)}")
        
    def completed_course(self, name):
        if name in self.students:
            self.students.remove(name)
            print(f"{name} has completed {self.course} course.")
        else:
            print(f"{name} is not an member of the course")
            
    def avg_grade(self,grades):
        total = sum(grades)
        average = total/len(grades)
        print(f"the average grade is: {average}")
        
course_input = input("Enter a course: ").lower()
name = input("Enter a instructor: ").lower()    
student = input("Enter a name: ").lower() 
course = onlinecourse(course_input,name)
grades = [90,86,92,78,80]

course.avg_grade(grades)
course.enroll_students(student)   
course.course_details()

    