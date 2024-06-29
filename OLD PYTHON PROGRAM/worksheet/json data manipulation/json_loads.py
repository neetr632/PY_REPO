# Import the 'json' module for JSON deserialization
import json

# Define a JSON-formatted string 'd'
d = '{ "course_name":"python", "fees":15000, "duration":"2 Months"}'

# Use json.loads() to deserialize the JSON-formatted string 'd' to a Python dictionary
f = json.loads(d)

# Print the type and the deserialized dictionary
print(type(f))
print(f)

for a in f:
    print(a,f[a])