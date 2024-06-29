import random
import string 

def random_string_list(length=9):
    random_string_list = random.choices(string.ascii_letters + string.digits, k=length)
    result = ''.join(random_string_list)
    print(result)

random_string_list()