input_file = open("random_text.txt","a") #append
input_file.write("Now the file has more content!")
input_file = open("random_text.txt","r") #read
print(input_file.read())
input_file.close()