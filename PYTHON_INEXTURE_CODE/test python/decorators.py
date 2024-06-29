# Define a decorator function
def my_decorator(func):
    def wrapper():
        print("Before calling the function")
        func()  # Call the original function
        print("After calling the function")
    return wrapper

# Apply the decorator using the @ syntax
@my_decorator
def say_hello():
    print("Hello!")

# Call the decorated function
say_hello()
