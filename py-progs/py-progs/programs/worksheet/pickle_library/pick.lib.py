# Import the 'pickle' module for working with binary data serialization
import pickle

# Create a list of numbers
l = [10, 20, 30, 40, 50]

# Open a file named "writedata.txt" in binary write mode ('wb')
file = open("writedata.txt", "wb")

# Use pickle.dump to serialize and write the list 'l' to the file
pickle.dump(l, file)

# Close the file to ensure changes are saved
file.close()
