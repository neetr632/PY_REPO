def read_file(file_path, num_lines=5):
    """Generator function to read the first `num_lines` lines of a text file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        for i, line in enumerate(file):
            if i >= num_lines:
                break
            yield line.strip()

# Usage
file_path = 'D:\SPACY\Training_data\data\hi\hi.txt'
for line in read_file(file_path, 5):  # Only read the first 5 lines
    print(line)
