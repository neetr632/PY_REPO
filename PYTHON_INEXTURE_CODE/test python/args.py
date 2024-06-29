def variable_length_of_args(*args):
    for arg in args:
        if isinstance(arg, str):
            print("str catch by function") 
        elif isinstance(arg, int):
            print("int catch by function")
        elif isinstance(arg, float):
            print("float catch by function")
        else:
            print(f"other type ({type(arg).__name__}) caught by function")
        
variable_length_of_args("hello", "how", "are", "you",3,5,8,7.0)

# star args allows you to accept the positional arguments in any order 

