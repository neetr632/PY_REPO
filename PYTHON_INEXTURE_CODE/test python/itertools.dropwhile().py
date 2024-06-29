from itertools import dropwhile, takewhile, filterfalse

def should_drop(x):
    return x < 1

for i in dropwhile(should_drop, [-1, -2, -2, -4, 21, -1, 0, 1, 2, -2, 56]):
    print(i, end=" ")
    
print("\n" "take while func will have the opposite effect of dropwhile")

for i in takewhile(should_drop, [-1, -2, -2, -4, 21, -1, 0, 1, 2, -2, 56]):
    print(i, end=" ")
# the condition becomes false them all the values will be printed regardless of the values left in the iiterator

print("\n" "the filter func will have filtered items")
for i in filter(should_drop, [1, 2, 4, 5, 7, 8, 9, 0, -1, 2, 3, 4, 5, -2]):
    print(i, end=" ")

print("\n" "the filterfalse func will have filtered items in the reverse order")  # t
for i in filterfalse(should_drop, [1, 2, 4, 5, 7, 8, 9, 0, -1, 2, 3, 4, 5, -2]):
    print(i, end=" ")

