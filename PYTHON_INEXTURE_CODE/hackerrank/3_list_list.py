scores = []
list_1 = []
for _ in range(int(input())):
    scores.clear()
    name = input()
    score = float(input())
    scores.append(name)
    scores.append(score)
    list_1.append(scores[:])

sorted_list = sorted(list_1, key=lambda x: x[1])
new_list = []
length = len(sorted_list)
for i in range(length - 1):
    if sorted_list[i][1] == sorted_list[i + 1][1]:
        new_list.append(sorted_list[i])
        new_list.append(sorted_list[i + 1])

new_list.sort()
print(new_list[0])
