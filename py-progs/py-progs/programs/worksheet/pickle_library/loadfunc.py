# Import the 'pickle' module for serialization and deserialization
import pickle

# Open the file 'writedata.txt' in binary read mode ('rb')
file = open("writedata.txt", "rb")

# Load (deserialize) the data from the file using pickle
l = pickle.load(file)

# Print the deserialized data
print(l)

# Close the file
file.close()
