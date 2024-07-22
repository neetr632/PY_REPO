# Print True if p(x)= k . Otherwise, print False.
# Enter your code here. Read input from STDIN. Print output to STDOUT

variables = input().split()
x, k = int(variables[0]), int(variables[1])

expression_list = input().split()
expression = "".join(expression_list)
if eval(expression) == k:
    print(True)
else:
    print(False)
