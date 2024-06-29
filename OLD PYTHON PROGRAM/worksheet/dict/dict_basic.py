# creation of a dictionary storing info about jhon doe.
my_dict = {
    "name": "jhon doe",
    "age": 30,
    "occupation": "software engineer",
}
# Accessing individual key-values pairs
name = my_dict["name"]
age = my_dict["age"]
occupation = my_dict["occupation"]
# printing the accessed values
print(f"Name:{name}")
print(f"Age:{age}")
print(f"Occupation:{occupation}")
# creating two empty lists to store the keys and values seperately
list_of_keys = []
list_of_values = []
# for loop to iterate both keys and values at the same time
for keys, values in my_dict.items():  # items() used to iterate both key's and values at the same time
    print(f"{keys} :- {values} <== printed with the help of 'for' loop", keys)
    # append used to store the keys iterated in the dict
    list_of_keys.append(keys)
    # append used to store the key's values iterated in the dict
    list_of_values.append(values)

# lists will be printed here
print("list of keys in my_dict:-", list_of_keys)
print("list of values in my_dict:-", list_of_values)

my_dict_2 = {
    "name": "mike",
    "age": 3,
    "occupation": "toddler",
}
# printing only the keys
for a in my_dict_2.keys():
    print(f"this will print the key's :-", a)
# printing only the values
for a in my_dict_2.values():
    print(f"this will print the key's value:-", a)
# getting individual keys values without for loops
unknown = my_dict_2.get("profession")
print(unknown)

