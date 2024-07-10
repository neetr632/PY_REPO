import string
def print_rangoli(size):
    alphabets = string.ascii_lowercase
    list_of_alphabets = list(alphabets)[:size]
    
    for i in range(size):
        left_part = "-".join(list_of_alphabets[size-i-1:size][::-1] + list_of_alphabets[size-i:size]) #[x:x] = produces an empty list even if there are elements in the list
        #'list'[::-1] = reverses the list that are preceding it
        line = left_part.center(4*size-3, "-") #to calculate the center values we need to count the alphabets and hypens and
        print(line)
    for i in range(size-1, 0, -1): #range(start, stop, step) since the middle line will be printed by the above loop we needn't print the middle line here again.
        #start the loop in the reverse order with a step of -1 starting with one less value than the size of the list
        left_part = "-".join(list_of_alphabets[size-i:size][::-1] + list_of_alphabets[size-i+1:size])
        line = left_part.center(4*size-3, "-")
        print(line)
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)