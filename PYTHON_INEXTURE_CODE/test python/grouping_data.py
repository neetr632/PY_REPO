from itertools import groupby


data = [1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5]

grouped_data = groupby(data)

for key, group in grouped_data:
    print(f"KEY:{key}: GROUP:{list(group)}")
    
