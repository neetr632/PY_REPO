with open("sample.txt", "r") as f:
    text = f.read()
    last_bytes = text[-15:]
    current_position = f.tell()
    f.seek(current_position - 8)
    more_data = f.read()
    print(last_bytes)
    print(more_data)