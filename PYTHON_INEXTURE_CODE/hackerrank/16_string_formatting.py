def print_formatted(number):
    for i in range(1, number+1):
        binary = bin(number)[2:]
        length = len(binary)
        print(f"{str(i).rjust(length)} {(oct(i)[2:]).rjust(length)} {((hex(i)[2:]).upper()).rjust(length)} {(bin(i)[2:]).rjust(length)}")

# n = int(input())
print_formatted(33)