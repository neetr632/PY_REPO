# Create a dictionary named "d" with custom key-value pairs
d = dict(
    name="python",  # name of the programming language
    fees=8000,  # course fees
    profession="programming language",  # description of the language
    age=32,  # age of the language
    users="students, corporates, programmers",  # who uses this language
)

# Print the dictionary
print(f"Dictionary before updates: {d}")

# Update the value for the "age" key
d.update({"age": 21})

# Add a new key-value pair with "desc" key and "this is a python" value
d["desc"] = "this is a python"

# Print the updated dictionary
print(f"Dictionary after updates: {d}")

# Clear the dictionary (remove all key-value pairs)
d.clear()

# Print the empty dictionary
print(f"Dictionary after clearing: {d}")
