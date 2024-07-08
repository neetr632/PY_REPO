# 7
# insert 0 12
# insert 1 15
# insert 2 20
# append 25
# print
# remove 15
# print

N = int(input())
my_list = []

for i in range(N):
    operation = input().split()
    if operation[0] == "insert":
        my_list.insert(int(operation[1]), int(operation[2]))
    elif operation[0] == "append":
        my_list.insert(int(operation[1]))
    elif operation[0] == "remove":
        my_list.remove(int(operation[1]))
    elif operation[0] == "print":
        print(my_list)
    elif operation[0] == "sort":
        my_list.sort()
    elif operation[0] == "reverse":
        my_list.reverse()
    elif operation[0] == "pop":
        my_list.pop()

print(my_list)
