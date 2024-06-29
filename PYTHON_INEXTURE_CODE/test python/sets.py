basket = {"apple", "apple", "orange", "pear", "orange", "banana"}
print(basket)

print("adding elements")
basket.add("kiwi")
print(basket)

print("removing elements from the sets")
basket.remove("orange")
print(basket)

basket.discard("apple")
print(basket)

basket.pop()
print(basket)

print("set methods realted to the subset of elements")
set_1 = {1,24,42,4,36,4,579,8,25,645,623,453,573,53,343}
set_2 = {579,8,25,645,623}

set_result = set_2.issubset(set_1)
print(f"the set_2 is subset of the set_1...?:- {set_result}")

set_result_1 = set_1.issuperset(set_2)
print(set_result_1)
"""Adding Elements:

add(element)
Removing Elements:

remove(element)
discard(element)
pop()
Checking Membership:

issubset(other_set)
issuperset(other_set)
in(element) (or element in set_name)
Set Operations (Modifying the Original Set):

update(other_set)
intersection_update(other_set)
difference_update(other_set)
symmetric_difference_update(other_set)
Other Methods:

clear()
copy()
frozenset(set_name)
union(other_set) (returns a new set)
intersection(other_set) (returns a new set)
difference(other_set) (returns a new set)
symmetric_difference(other_set) (returns a new set)
isdisjoint(other_set)"""
