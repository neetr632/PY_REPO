input_file = open("sample.txt","w")
list1=[]
for i in range(5):
    name = input("Enter your name: ")
    list1.append(name+"\n")
input_file.writelines(list1)
input_file.close() 