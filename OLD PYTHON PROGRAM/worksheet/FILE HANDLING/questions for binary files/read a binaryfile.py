import pickle
with open("student_records.dat" ,"rb") as input_file:
    data = pickle.load(input_file)
    print(data) 