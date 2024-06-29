import subprocess

powershell_code = '''
# Get computer information and save it to a text file
Get-ComputerInfo | Out-File -FilePath "computer_info.txt"

# Get information about BIOS and save it to a text file
Get-WmiObject Win32_BIOS | Out-File -FilePath "bios_info.txt"

# Get information about processes and save it to a text file
Get-Process | Out-File -FilePath "process_info.txt"

# Get information about services and save it to a text file
Get-Service | Out-File -FilePath "service_info.txt"

# Get information about network adapters and save it to a text file
Get-NetAdapter | Out-File -FilePath "network_adapter_info.txt"

# Get information about volumes and save it to a text file
Get-Volume | Out-File -FilePath "volume_info.txt"

# Get information about installed hotfixes and save it to a text file
Get-HotFix | Out-File -FilePath "hotfix_info.txt"

# Get information about IPv4 addresses and interfaces and save it to a text file
# Get-NetIPAddress -AddressFamily IPv4 | Out-File -FilePath "IPv4 Addresses"

'''

# Run the PowerShell code
result = subprocess.run(['powershell', '-Command', powershell_code], capture_output=True, text=True)

# Check the output and return code
if result.returncode == 0:
    print("PowerShell script executed successfully:")
    print(result.stdout)
else:
    print("Error executing PowerShell script:")
    print(result.stderr)
