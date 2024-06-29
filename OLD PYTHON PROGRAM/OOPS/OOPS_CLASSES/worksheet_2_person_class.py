# Write a  Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age
from datetime import date
class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob
    # Calculate the age of the person based on their date of birth

    def get_age(self):
        today = date.today()
        age = today.year - self.dob.year
        if today < date(today.year, self.dob.month, self.dob.day):
            age -= 1
        return age
    # Print the details of the person
    def print_details(self):
        print("the person name is:", self.name)
        print("the person age is:", self.get_age())
        print("the person dob is:", self.dob)
        print("the person country is:", self.country)

person = Person("John", "USA", date(1990, 5, 15))
person.print_details()