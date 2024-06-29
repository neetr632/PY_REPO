import collections

dict1 = { 'a' : 1, 'b' : 2 } 
dict2 = { 'b' : 3, 'c' : 4 } 
chain = collections.ChainMap(dict1, dict2)

print(chain)

print(list(chain.keys())) #b is repeated therefore the results have 1 value.
print(list(chain.values()))


c = collections.ChainMap({'a': 1, 'b': 2, 'c': 3}) #create a new chain map with a dict and assigning it to c.
d = c.new_child({'d': 4,'e': 5, 'f': 6}) #modifying existing chain map with a dict and assigning it to d.

e = d.new_child({'g': 7, 'h': 8})
print(e)


combined = c.maps + d.maps
combined_maps = collections.ChainMap(*combined)
print(f"this is a combined chain maps:- {combined}")

#GET THE FIRST KEY

iterator = iter(combined_maps)
first_key = next(iter(iterator))
second_key = next(iter(iterator))
print(f"first key:- {first_key}")
print(f"second key:- {second_key}")

for item in iter(iterator):
    print(f"item: {item}")
    
for item in combined_maps.items():
    print(f"item: {item}")
    
combined_maps['g']= 4
combined_maps['h']= 5

print(combined_maps) #adding elements to the ChainMap

