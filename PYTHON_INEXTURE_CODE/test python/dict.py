a = {"a": 12, "b": 13, "c": 14, "d": 15}
print(a)
print(type(a))

"""ways to access keys in dictionary"""
print(list(a.keys()))
print(list(a))

""" accessing items through keys in dictionary"""
print(a["a"])
print(a.get("a"))
print(a["b"])
print(a.get("b"))
print(a["c"])
print(a.get("c"))
print(a["d"])
print(a.get("d"))
print(a.get("e", "key not present in dictionary"))
"""print(a["e"])"""

'''cahnging value at key in dictionary'''
a["a"] = 121
print(f"the value at key 'a' is changed from 11 to :-{a["a"]}")

if 'a' in a:
    print("the value at key 'a' is present in dictionary")
    
popit = a.pop('a', "key not present in dictionary")
print(popit)
print(a)

key_value = a.popitem()  # return a tuple with key and value. if dict is empty raise keyerror
print("Popped last item is: \n{}\n".format(key_value))