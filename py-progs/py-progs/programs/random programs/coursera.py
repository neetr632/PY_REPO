IP = ["198.223.0.0", "198.223.0.1", "198.223.0.2", "198.223.0.3", "198.223.0.4", "198.223.0.5", "198.223.0.6", "198.223.0.7",
    "198.223.0.8", "198.223.0.9", "198.223.0.10", "198.223.0.11", "198.223.0.12", "198.223.0.13", "198.223.0.14", "198.223.0.15",
    "198.223.1.0", "198.223.1.1", "198.223.1.2", "198.223.1.3", "198.223.1.4", "198.223.1.5", "198.223.1.6", "198.223.1.7",
    "198.223.1.8", "198.223.1.9", "198.223.1.10", "198.223.1.11", "198.223.1.12", "198.223.1.13", "198.223.1.14", "198.223.1.15",]

network = []
matching_ip = []
sub_string_1 = "223.3"
sub_string_2 = "1.8"

for address in IP:
    network.append(address[0:3])

# Print the network list once after processing all IP addresses
print(network)

for address in IP:
    if sub_string_1 in address or sub_string_2 in address:
        matching_ip.append(address)

# Print the matching_ip list
print(matching_ip)
