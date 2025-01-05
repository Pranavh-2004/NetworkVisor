import scapy.all as scapy

def arp_scan(target_ip):
    """
    Perform an ARP scan on the provided target IP address or subnet.
    Returns a list of discovered devices with their IP, MAC, and Hostname.
    """
    arp_request = scapy.ARP(pdst = target_ip) # Creates an ARP request packet
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") # Broadcasts an ethernet frame
    packet = broadcast / arp_request # Combine ARP request and Ethernet frame
    answered_list = scapy.srp(packet, timeout=1, verbose=False)[0] # Send and recieve packets

    devices = []
    for sent, recieved in answered_list:
        device_info = {
            "ip": recieved.psrc,
            "mac": recieved.hwsrc
        }
        devices.append(device_info)

    return devices