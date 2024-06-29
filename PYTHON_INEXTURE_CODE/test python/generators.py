
def read_large_file(file):
    with open(file) as f:
        for line in f:
            yield line

large_file_generator = read_large_file('text.txt')


for line in large_file_generator:
    print(line, end=' ')