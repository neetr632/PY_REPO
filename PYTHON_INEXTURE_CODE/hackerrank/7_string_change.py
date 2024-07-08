def swap_case(s):
    return_this = s.swapcase()
    return return_this

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)