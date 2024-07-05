students = []
for _ in range(int(input())):
    name = str(input())
    try:
        score = input()
        if "." in score:
            score = float(score)
        else:
            score = int(score)
        students.append([name, score])
    except ValueError:
        print("Invalid input! Please enter a valid number for score.")
print(f"unsorted_list:-{students}")

sorted_list = sorted(students, key=lambda x: x[1])

print(f"sorted_list:- {sorted_list}")
print(f"student with 2nd highest marks:- {sorted_list[1][0]}")
length = len(sorted_list)
print(f"length of the nested list:- {length}")
