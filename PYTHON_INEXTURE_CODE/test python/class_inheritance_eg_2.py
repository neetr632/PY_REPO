# The code defines classes A and B where class B inherits from class A, allowing for updating and deleting Entries
# displaying details of individuals.
class A:
    def __init__(self):
        self.name = None  # Providing A Default State To The instance variables is a good practice
        self.age = None
        self.gender = None
        self.record_no = 0
        self.details_list = []

    def details(self, name, age, gender):
        self.record_no += 1
        self.name = name
        self.age = age
        self.gender = gender
        record = {
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "record_number": self.record_no,
        }
        self.details_list.append(record)
        if self.record_no >= 3:
            print(self.details_list)
        else:
            pass


class B(A):
    def update_dict(self, record_no, key, value):
        for x in self.details_list:
            if x["record_number"] == record_no:
                x[key] = value

    def updated_dict(self):
        print(self.details_list)

    def delete_dict_entries(self, record_no, key):
        for x in self.details_list:
            if x["record_number"] == record_no:
                del x[key]


thread = B()
thread.details(name="Alice", age=25, gender="female")
thread.details(name="bob", age=25, gender="male")
thread.details(name="marry", age=25, gender="female")

thread.update_dict(1, "name", "kyle")

print("after_delete_dict:-")
thread.delete_dict_entries(2, "age")

print("updated_dict:- ")
thread.updated_dict()
