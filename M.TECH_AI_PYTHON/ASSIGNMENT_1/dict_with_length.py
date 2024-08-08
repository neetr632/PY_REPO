x = int(input("Enter the numbers of strings you want to enter:- "))
my_dict = {}
while x > 0:
    string = str(input("enter your string:- "))
    str_len = len(string)
    my_dict[string] = str_len
    x -= 1
print(my_dict)