import string
def print_rangoli(size):
    alphabets = string.ascii_lowercase
    list_of_alphabets = ",".join(alphabets).split(",")
    print(list_of_alphabets)
    for i in range(size):
        print("-".join(list_of_alphabets[size-1-i:size]).center(4*size-3, "-"))
# n = int(input())
print_rangoli(5)
