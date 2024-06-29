import collections

c = collections.ChainMap({"a": 1, "b": 2, "c": 3})
d = c.new_child({"d": 4, "e": 5, "f": 6})
e = d.new_child({"g": 7, "h": 8})

print(e["f"])  # chain map performs lookup in child maps too.
del e.maps[1]["d"]
e["i"] = 9  # adding a new key to the first dictionary directly.
e.maps[1]["d"] = 69  # adding new keys at deeper level in chain map... using the index of the dicts
print(e)
