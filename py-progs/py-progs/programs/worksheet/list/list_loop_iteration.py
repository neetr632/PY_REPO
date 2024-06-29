w = [10,123,24,234,45,23,67,43556]
reverse_string = [10,123,24,234,45,23,67,43556,10,123,24,234,45,23,67,43556]
y = len(reverse_string)
print(y)
even_numbers=[]
odd_numbers=[]
for n in w:
    if n%2==0 :
        even_numbers.append(n)
    else:
        odd_numbers.append(n)
        
print("Even Numbers list:-",even_numbers)
print("odd Numbers list:-",odd_numbers)
print("**************new line*****************")
print("this string is printed in reverse")
for m in range(y-1,-1,-1):
    print(reverse_string[m])