k = int(input())
string = "AABCAAADA"
for i in range(len(string)):
    while len(string) > k: 
        print(string[:k])
    