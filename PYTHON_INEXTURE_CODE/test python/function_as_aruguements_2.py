def func_1(text):
    return text.upper()

def func_2(text):
    return text.lower()

def call_them(func):
    greeting = func("this is a call-by another function")
    print(greeting)
    
call_them(func_1)
call_them(func_2)

#function is passed to another function  