a_list = list(range(1, 11))
print(a_list[:]) 
# print every item in the list
a_list_b = list(range(0, 11))
print(a_list[5:]) #5-last
#print from the 5th index to the last index
print(a_list[:6]) #0-6
# print from 0th index to 6th index \
print(a_list[2:7]) #2-7
# print from the 2nd index to the 7th index
print(a_list_b[2:50:5]) #2-50 with 5steps
#start_index stop_index step_index 

print(a_list_b[::7]) #0-90 with 7steps
#is index is positive print from 0th index to the last index 
#taking every 7th index

"""negative indexes"""

print(a_list_b[-5:]) #print last 5 elements
print(a_list_b[-10:]) #print last 10 elements
