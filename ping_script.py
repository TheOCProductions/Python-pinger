import os
import time

# get user input for IP address
ip = input("Enter the IP address to ping: ")

# print available ports
ports = {
    1: 80,
    2: 443,
    3: 22,
    # add more ports as needed
}
print("Available ports:")
for i, port in ports.items():
    print(f"{i}. {port}")

# get user input for port selection
port_choice = int(input("Select a port to ping: "))

# use paping to ping the selected port in a loop
port = ports.get(port_choice)
if port:
    while True:
        os.system(f"paping {ip} -p {port}")
        time.sleep(1)
else:
    print("Invalid port selection.")
