file_names = ["system_info.txt.encrypted", "clipboard_info.txt.encrypted", "mouse_info.txt.encrypted", "bios_info.txt.encrypted", "computer_info.txt.encrypted",
            "hotfix_info.txt.encrypted", "process_info.txt.encrypted", "service_info.txt.encrypted", "volume_info.txt.encrypted", "network_adapter_info.txt.encrypted", "screenshot.png.encrypted", "key_log.txt.encrypted", "audio_info.wav.encrypted" , "specific_occurrence.txt.encrypted"]

# Remove ".encrypted" from each file name
file_names_without_extension = [file_name.replace('.encrypted', '') for file_name in file_names]

# Print the modified list
print(file_names_without_extension)
