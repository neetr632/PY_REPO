def myDecorator(x):
    def wrapper():
        print("you've entered the wrapper function")
        x() # this is place where the actual function is called
        print("you are exiting the wrapper function")
    return wrapper    
    
# apply the decorator using the @syntax
@myDecorator
def callee():
    print("decorator functions running")

callee()