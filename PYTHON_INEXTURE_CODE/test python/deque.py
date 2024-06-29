from collections import deque
print("""deque- a data structure from which the elements can be removed from both the sides""")


dq = deque()
dq = deque([1, 2, 3, 4, 5])
print(dq)
dq = deque('hello')
print(dq)

dq.appendleft(1)
dq.append(2)
print(dq)

print("extend a deque with other values")
dq.extend(['hello', 'world'])
print(dq)

dq.extendleft(['hello', 'world'])
print(dq)

dq.rotate(1)
print(dq)

dq.rotate(-1)
print(dq)

dq.insert(2,'hitler')

print(dq[0])
print(dq[2])
print(dq)

sliding_window = deque(maxlen=15)

for i in range(20):
    sliding_window.append(i)
    print(sliding_window)
    

