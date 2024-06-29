# Import the 'json' module for JSON decoding
import json

# Define the path to the JSON file
json_file_path = r"C:\Users\neham\OneDrive\Desktop\py-progs\worksheet\json data manipulation\2019-04-22_15-15-48_UTC.json"

try:
    # Open the file in read mode using a 'with' statement
    with open(json_file_path, "r") as file:
        # Read the contents of the file
        x = file.read()
        # Deserialize the JSON-formatted string to a Python dictionary
        final_data = json.loads(x)
        # Print the resulting dictionary
        print(final_data)

# Handle the specific exception when the file is not found
except FileNotFoundError:
    print(f"File not found: {json_file_path}")

# Handle the specific exception for JSON decoding errors
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")

# Handle general exceptions
except Exception as e:
    print(f"An unexpected error occurred: {e}")
