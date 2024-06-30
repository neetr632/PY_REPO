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

# Find the second lowest score
second_lowest_score = sorted_list[0][1]
for i in range(1, len(sorted_list)):
    if sorted_list[i][1] > second_lowest_score:
        second_lowest_score = sorted_list[i][1]
        break

# Collect names with the second lowest score
new_list = [student for student in sorted_list if student[1] == second_lowest_score]

# Sort alphabetically by name and print the names
new_list.sort()
for student in new_list:
    print(student[0])
