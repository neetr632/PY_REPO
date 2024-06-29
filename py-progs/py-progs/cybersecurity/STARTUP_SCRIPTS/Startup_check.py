import os
import sys

# Function to open the Startup folder in file explorer
def open_startup_folder():
    # Get the path to the Startup folder
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

    # Open the Startup folder in file explorer
    os.startfile(startup_folder)

# Function to check if script is in Startup folder
def check_startup():
    # Get the path to the Startup folder
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

    # Check if the script exists in the Startup folder
    script_path = os.path.join(startup_folder, os.path.basename(sys.argv[0]))
    if os.path.exists(script_path):
        print("Script is in the Startup folder.")
    else:
        print("Script is not in the Startup folder.")

if __name__ == "__main__":
    # Check if script is in Startup folder
    check_startup()

    # Open the Startup folder in file explorer
    open_startup_folder()
