try:
    # Open the file in read mode
    file = open("test.txt", "r")
    file_contents = file.read()
    print(file_contents)
except FileNotFoundError:
    print("The file 'test.txt' does not exist.")
