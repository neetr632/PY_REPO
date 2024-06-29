dict = {
    "name":"python",
    'fees':'67000',
    'duration':'2 months' 
}

popped_element = dict.pop('fees')
print(popped_element)

del dict["name"]
print(dict)