# import socket
# import re
# import requests

# # Function to resolve MAC address to vendor
# def get_mac_vendor(mac):
#     """
#     Returns the vendor name based on the MAC address.
#     Uses an external database for MAC address to vendor lookup.

#     :param mac: MAC address in the format XX:XX:XX:XX:XX:XX
#     :return: Vendor name if found, else 'Unknown Vendor'
#     """
#     try:
#         oui_prefix = mac[:8].upper().replace(":", "-")
#         # Use a local database (e.g., nmap-mac-prefixes)
#         with open("/usr/share/nmap/nmap-mac-prefixes", "r") as f:
#             for line in f:
#                 if line.startswith(oui_prefix):
#                     return line.strip().split("\t")[-1]
#     except FileNotFoundError:
#         pass
#     return "Unknown Vendor"


# # Function to resolve IP address to hostname
# def resolve_hostname(ip):
#     """
#     Resolves an IP address to a hostname using reverse DNS lookup.

#     :param ip: IP address (e.g., "192.168.1.1")
#     :return: Hostname if resolved, else 'Unknown Hostname'
#     """
#     try:
#         hostname = socket.gethostbyaddr(ip)[0]
#         return hostname
#     except socket.herror:
#         return "Unknown Hostname"


# # Function to validate IP address format
# def is_valid_ip(ip):
#     """
#     Validates if the given string is a valid IP address.

#     :param ip: IP address as string
#     :return: True if valid IP, else False
#     """
#     regex = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
#     return re.match(regex, ip) is not None


# # Function to ping an IP address
# def ping_ip(ip):
#     """
#     Pings an IP address to check if it's reachable.

#     :param ip: IP address as string
#     :return: True if reachable, else False
#     """
#     response = os.system(f"ping -c 1 {ip}")
#     return response == 0


# # Function to get external IP using an API
# def get_external_ip():
#     """
#     Returns the external public IP address by querying an external service.

#     :return: Public IP address as a string
#     """
#     try:
#         response = requests.get('https://api.ipify.org?format=json')
#         return response.json()['ip']
#     except requests.RequestException:
#         return "Unable to fetch external IP"