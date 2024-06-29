


print("lets replace the current value with something else:- {} {}".format("curly", "braces"))
placeholder = "value provided by the variable"

print("i need a value here: {}".format(placeholder))

placeholder_1 = 12
placeholder_2 = 13

print("i need a value here: {1} and {0}".format(placeholder_1,placeholder_2))

list_of_dict =[{"a": 1, "b" : 2, "c" : 3, "d" : 4}, {"e":5,"f":6,"g":7,"h":8},{"i":9,"j":10,"k":11,"l":12}]
print("i can put anything here form list of dicts {}" .format(list_of_dict[1]))

a = [34,"A",3,46,25,'µ']
print("values are converted to string before printing them by using '!s conversion flag':- {0!s} ".format(a))
print("the values area after the repr is:- {arg!r}".format(arg=a))
print("More {0!a}".format(a))

string_1 = "this is a string that needs to be {:<40}string"
print(string_1.format("aligned to the left of the screen"))

string_2 = "this is a string that needs to be {:>40}string"
print(string_2.format("aligned to the right of the screen"))

string_3 = "this is a string that needs to be shifted to the {:^40}screen"
print(string_3.format("centered"))


