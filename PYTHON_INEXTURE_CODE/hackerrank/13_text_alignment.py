# This Python code snippet is creating a pattern using the character 'H' based on the input value of
# `thickness`. Here is a breakdown of what each part of the code is doing:
thickness = int(input()) 
c = 'H'

for i in range(thickness):
    print(((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1)).center(thickness * 2))

for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

for i in range((thickness + 1) // 2):
    print((c * thickness * 5).center(thickness * 6))

for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

for i in range(thickness):
    print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).center(thickness * 10))
