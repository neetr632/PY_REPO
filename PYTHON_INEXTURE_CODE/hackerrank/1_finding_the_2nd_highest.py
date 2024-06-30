# This code snippet is a Python script that takes user input, processes it, and then prints out the
# second largest unique integer from the input. Here's a breakdown of what each part of the code does:
if __name__ == '__main__':
    count = int(input())
    user_input = input()
    input_list = user_input.split() 
    unique_list = list(dict.fromkeys(map(int,input_list)))
    unique_list.sort(reverse=True)
    print(unique_list[1])

