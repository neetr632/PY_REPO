with open("file1.txt", "w") as f1:
    for i in range(100):
        f1.write("hello this is a new file with multiple words and repeated over multiple times\n")
with open("file2.txt", "w") as f1:
    for i in range(100):
        f1.write("ive been written multiple times")