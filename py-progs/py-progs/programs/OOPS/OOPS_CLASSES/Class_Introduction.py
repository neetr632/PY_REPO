class App:  # no parantheses are needed and class c should be in small letters
    def __init__(self, users, username, login, storage): #create three methods for the app class
        self.username = username
        self.users = users
        self.storage = storage
        self.login = login

def login(self):
    if self.username == "owner" and self.users >=1:
        print("welcome to the account.")
    else:
        print("login failed")

def increase_capacity(self, number):
    self.storage += number
    return self.storage
    
product_one = App(35,"owner",True,256)
product_one.login()
product_one.increase_capacity(50)
 