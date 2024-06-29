import shutil
import os

def copy_txt_files(source_dir, dest_dir, txt_file_names):
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    for file in txt_file_names:
        source_file_path = os.path.join(source_dir, file)
        destination_file_path = os.path.join(dest_dir, file)
        shutil.copy(source_file_path, destination_file_path)
        print(f"TXT_File '{file}' copied successfully.")

def copy_encrypted_files(source_dir, dest_dir, encrypted_file_names):
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    for file in encrypted_file_names:
        source_file_path = os.path.join(source_dir, file)
        destination_file_path = os.path.join(dest_dir, file)
        shutil.copy(source_file_path, destination_file_path)
        print(f"Encrypted_File '{file}' copied successfully ")

source_dir = r'C:\Users\neham\OneDrive\Desktop\py-progs\cybersecurity'
dest_dir_1 = "TXT_FILES"
dest_dir_2 = "ENCRYPTED_FILES"

txt_file_names = ['system_info.txt', 'clipboard_info.txt', 'mouse_info.txt', 'bios_info.txt', 'computer_info.txt', 'hotfix_info.txt', 'process_info.txt',
                  'service_info.txt', 'volume_info.txt', 'network_adapter_info.txt', 'screenshot.png', 'key_log.txt', 'audio_info.wav', 'specific_occurrence.txt']
encrypted_file_names = ["system_info.txt.encrypted", "clipboard_info.txt.encrypted", "mouse_info.txt.encrypted", "bios_info.txt.encrypted", "computer_info.txt.encrypted",
                        "hotfix_info.txt.encrypted", "process_info.txt.encrypted", "service_info.txt.encrypted", "volume_info.txt.encrypted", "network_adapter_info.txt.encrypted", "screenshot.png.encrypted", "key_log.txt.encrypted", "audio_info.wav.encrypted", "specific_occurrence.txt.encrypted"]

copy_txt_files(source_dir, dest_dir_1, txt_file_names)
copy_encrypted_files(source_dir, dest_dir_2, encrypted_file_names)
