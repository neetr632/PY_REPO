def func1():
    print("Function 1 called")

def func2():
    print("Function 2 called")

def main():
    print("Running module1.py as a script")
    func1()
    func2()

# Check if the script is being run directly
if __name__ == "__main__":
    main()  # Call the main function if running as a script
