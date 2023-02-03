import requests
import json
import subprocess

# Get a list of VPN servers from the ProtonVPN API
response = requests.get("https://api.protonmail.ch/vpn/logicals")
server_list = json.loads(response.text)

# Choose a random VPN server and get its configuration

server = "yNLCqBR-zq71WthT9WjWNTJWLS1zFFlUKtShW4qSJS1ecpqzzc_lD5t9rVRiL-zQY4oe3-MCpaMn9jSz-G-ZRw=="
config = requests.get(f"https://api.protonmail.ch/vpn/configs/{server}.ovpn").text

# Save the configuration to a file
with open("vpn.ovpn", "w") as f:
    f.write(config)

# Connect to the VPN server using the ProtonVPN CLI
subprocess.run(["protonvpn-cli", "--connect", "vpn.ovpn"])