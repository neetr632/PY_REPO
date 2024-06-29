def check_file_signature(file_path, expected_signature):
    with open(file_path, 'rb') as file:
        # Read the first few bytes of the file
        file_signature = file.read(len(expected_signature))
        
        # Compare the read signature with the expected signature
        if file_signature == expected_signature:
            print(f"The file signature matches the expected signature: {expected_signature}")
            return True
        else:
            print(f"The file signature does not match the expected signature: {expected_signature}")
            return False

# Example usage:
# Specify the file path and the expected signature
file_path = 'C:\\Users\\neham\\OneDrive\\Desktop\\py-progs\\programs\\worksheet\\FILE_SIGNATURE\\1-747x221.png'
expected_signature = b'\x89PNG\r\n\x1a\n'

# Check the file signature
check_file_signature(file_path, expected_signature)
