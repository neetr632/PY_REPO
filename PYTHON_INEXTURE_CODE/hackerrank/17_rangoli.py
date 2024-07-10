import string
def print_rangoli(size):
    alphabets = string.ascii_lowercase
    list_of_alphabets = list(alphabets)[:size]
    
    for i in range(size):
        left_part = "-".join(list_of_alphabets[size-i-1:size][::-1] + list_of_alphabets[size-i:size])
        line = left_part.center(4*size-3, "-")
        print(line)
    for i in range(size-1, 0, -1):
        left_part = "-".join(list_of_alphabets[size-i:size][::-1] + list_of_alphabets[size-i+1:size])
        line = left_part.center(4*size-3, "-")
        print(line)
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)