import sys  # Import the sys module, which provides access to system-specific parameters and functions
 
# Print the version of Python interpreter you're currently using
print(sys.version)

# Print the path to the Python interpreter executable
print(sys.executable)

# Print a tuple of the names of all modules built into this Python interpreter
print(sys.builtin_module_names)

# Print a dictionary that maps module names to modules that have already been loaded
print(sys.modules)

# Check if the 'time' module is already loaded (True if loaded, False otherwise)
print('time' in sys.modules)

# Check if the 'gtk' module is already loaded (True if loaded, False otherwise)
print('gtk' in sys.modules)
