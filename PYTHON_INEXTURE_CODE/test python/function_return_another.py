# CREATE A NESTING FUNCTION


def first_func(x):
    def second_func(y):
        return x + y
        # The closure property in Python allows an inner function to retain access to variables from its enclosing scope (the scope in which it was defined).
        # This property enables the inner function to "close over" or capture the values of variables, including arguments, from the outer function. As a result,
        # the inner function can access and utilize these captured variables even after the outer function has finished executing

    return second_func


second_func = first_func(14) #behaves as a callable function object. 
print(second_func(23)) 
print(type(second_func))  # <class 'function'>
