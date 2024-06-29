# Write a Python program that takes a list of numbers as input and counts
# how many of those numbers are even and how many are odd. Then, print the counts.
inputted_numbers = []
odd_number = []
even_number = []
num_count = int(input("enter the total numbers u want to add to count and filter them?...:- "))
for i in range(num_count):
    actual_number = int(input(f"Enter the number that you want to add {i+1}: "))
    inputted_numbers.append(actual_number)

for x in inputted_numbers:
    if x % 2 == 0:
        even_number.append(x)
    else:
        odd_number.append(x)
        

count_of_even_nos = len(odd_number)
count_of_odd_nos = len(even_number)
print(f"the inputted numbers by the user's are:- {inputted_numbers}")
print(f"the number of odd numbers:- {count_of_odd_nos}")
print(f"the number of even numbers:- {count_of_even_nos}")

