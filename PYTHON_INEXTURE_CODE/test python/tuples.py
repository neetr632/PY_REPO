tuples = (
    "hi",
    "lo",
    "mid",
    "left",
    "right",
    1,
    1,
    2,
    34,
    23,
    5,
    7,
    35,
    78,
    90,
    54,
    32,
    2,
    1,
    56,
    5,
    89,
    6,
)
count_of_1 = tuples.count(1)
print(count_of_1)

tuples_len = len(tuples)
print(tuples_len)

t = 12345, 54321, "hello"
print(t[0])

"""nested tuples"""
u = t, (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(u)

"""con contain multiple mutable objects"""
v = ([1, 2, 3], [3, 4, 5], [5, 6, 7])
print(v)

zisEmpty = ()
print(zisEmpty)

zisnotEmpty = ("hello",)
print(zisnotEmpty)

x, y, z = t
print(t)

"""example oof usage"""
print("unpacking a tuple to access it values")
product_info = ("shirt", "M", 15.99)
name, size, price = product_info
print(f"product_type: {name}, product_size: {size}, product_price: {price}$")

"""update tuple"""
my_set = {1, 2, 3}
other_set = {2, 4, 5, 8, 23}
my_set.update(other_set)
print(my_set)


'''minimum and maximum values from a tuple values'''
my_max = max(my_set)
print("max vlaue from tuple:-", my_max)
my_min = min(my_set)
print("min value from the tuple:-",my_min)

"""repeatation with a tuple single tuple values"""
new_my_set = zisnotEmpty * 4
print(new_my_set)