rows = 3
cols = 4
k = 1
arr = [
    [1, 12, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
temp=[]
for i in arr:
    temp.append(i[k])
temp.sort()

for i in range(len(arr)):
    arr[i][k] = temp[i]
    
print(arr)
        
    
    
    
