numbers = []
for _ in range(10):
    number = int(input("Enter an integer:- "))
    numbers.append(number)

sum_greater_than_10 = sum(x for x in numbers if x > 10)

print(f"the sum of the all the numbers greater than 10 is:- {sum_greater_than_10}")
