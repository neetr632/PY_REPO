x = str(input("enter the string:- "))
unique_chars = "".join(dict.fromkeys(x))
print(unique_chars)