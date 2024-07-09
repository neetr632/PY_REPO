check_this_string = str(input())

def is_lower(check_this_string):
    for char in check_this_string:
        if char.islower():
            return True
    return False  

def is_upper(check_this_string):
    for char in check_this_string:
        if char.isupper():
            return True
    return False
  
def is_digit(check_this_string):
    for char in check_this_string:
        if char.isdigit():
            return True
    return False
  
def is_alpha(check_this_string):
    for char in check_this_string:
        if char.isalpha():
            return True  
    return False  

def is_alnum(check_this_string):
    for char in check_this_string:
        if char.isalnum():
            return True
    return False    

print(is_lower(check_this_string))
print(is_digit(check_this_string))
print(is_alpha(check_this_string))
print(is_alnum(check_this_string))
print(is_upper(check_this_string))