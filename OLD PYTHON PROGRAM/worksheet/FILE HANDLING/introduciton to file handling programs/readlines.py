input_file = open("random_text.txt", "r")
i = 0
while i < 4:
    extracted_line = input_file.readline().strip()  # Remove newline and trailing whitespace
    print(extracted_line)
    i += 1
