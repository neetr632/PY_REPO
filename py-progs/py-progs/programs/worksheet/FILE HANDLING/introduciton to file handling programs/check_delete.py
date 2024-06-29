import os 
if os.path.exists("i_was_created_through_python"):
    os.remove("i_was_created_through_python_123.txt")
else:
    print("the file does not exist")