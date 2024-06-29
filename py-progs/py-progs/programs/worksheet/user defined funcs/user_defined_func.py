def simple_function():
    user_input = input("Enter your string or integer: ")
    print(user_input)

    for char in str(user_input): 
        #This converts the user input to a string. "str(user_input)"
        print(char)

def another_simplefunction():
    print("i was imported from a script to run")
    
if __name__ == "__main__":
    simple_function()
   
