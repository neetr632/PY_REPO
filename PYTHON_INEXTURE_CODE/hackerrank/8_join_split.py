def split_and_join(line):
    non_hypend_line = line.split(" ")
    print(non_hypend_line)
    line_hypend = "-".join(non_hypend_line)
    return line_hypend


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)