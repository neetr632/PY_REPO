from cryptography.fernet import Fernet
import os


def decrypt_files(key_file, encrypted_files, output_directory):
    # Load the key from the key file
    with open(key_file, "rb") as kf:
        key = kf.read()

    # Create a Fernet object with the key
    fernet = Fernet(key)
    # create a directory if not exist 
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for encrypted_file in encrypted_files:
        # Generate the output file path
        output_file = os.path.join(output_directory, f'decrypted_{
                                   os.path.basename(encrypted_file)}')

        # Read the encrypted file
        with open(encrypted_file, "rb") as ef:
            encrypted_data = ef.read()

        # Decrypt the file contents
        decrypted_data = fernet.decrypt(encrypted_data)

        # Write the decrypted data to the output file
        with open(output_file, "wb") as df:
            df.write(decrypted_data)

    print("Files decrypted successfully.")


# Example usage:
key_file = "key.key"  # Path to the key file used for encryption
encrypted_files = ["system_info.txt.encrypted", "clipboard_info.txt.encrypted", "mouse_info.txt.encrypted", "bios_info.txt.encrypted", "computer_info.txt.encrypted",
                   "hotfix_info.txt.encrypted", "process_info.txt.encrypted", "service_info.txt.encrypted", "volume_info.txt.encrypted", "network_adapter_info.txt.encrypted", "screenshot.png.encrypted", "key_log.txt.encrypted", "audio_info.wav.encrypted", "specific_occurrence.txt.encrypted"]  # List of encrypted files
output_directory = "decrypted_files"  # Directory to save the decrypted files

decrypt_files(key_file, encrypted_files, output_directory)
