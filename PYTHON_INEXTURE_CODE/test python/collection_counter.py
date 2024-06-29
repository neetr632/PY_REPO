import collections
from collections import Counter

C1 = Counter({"red": 4, "blue": 2,"green": 1})
C2 = Counter({"pink": 2, "yellow": 4, "crimson":2})

chain = collections.ChainMap(C1, C2)
print(chain['red'])
chain['blue'] += 1
print(chain['blue'])

total_red  = sum([c['red'] for c in chain.maps])
print(f"Total occurrences of red:- {total_red}")