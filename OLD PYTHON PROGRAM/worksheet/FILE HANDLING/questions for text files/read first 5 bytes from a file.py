with open("worksheet_1.txt","w+") as input_file:
    write_here = input("Enter your text here: ")
    input_file.write(write_here + "\n") # adding a new line command in the function is not neccesary since input is of one line.
    input_file.seek(0) # to shift the pointer to the beginning of the file. after a wtite process in a textfile.
    content = input_file.read(10)
    print(content)

# with open("worksheet_1.txt", "w+") as input_file:
#     write_here = input("What do you want to write to the file? ")
#     input_file.write(write_here + "\n")

    
# with open("worksheet_1.txt", "r") as input_file:   
#     input_file.seek(0)  # Reposition the pointer to the beginning
#     content = input_file.read(5)
#     print(content)

