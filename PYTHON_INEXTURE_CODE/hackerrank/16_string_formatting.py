def print_formatted(number):
    for i in range(1, number+1): #range(start, stop, step)
        print(f"{str(i).ljust(2)} {(oct(i)[2:]).ljust(2)} {((hex(i)[2:]).upper()).ljust(2)} {(bin(i)[2:]).ljust(2)}")  

# n = int(input())
print_formatted(17)