import pickle
stu={}
found = False
with open("student_records.dat", "rb+") as input_file:
    try:
        while True:
            rpos = input_file.tell()
            stu = pickle.load(input_file)
            if stu['marks']>=50:
                stu['marks']+=2
                input_file.seek(rpos)
                pickle.dump(stu,input_file)
                found = True
    except EOFError:
        if found == False:
            print("no such records found")
        else:
            print("successfully updated.")
    