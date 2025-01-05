import scapy.all as scapy
from socket import gethostbyname, getservbyport

def tcp_scan(target_ip, target_ports):
    """
    Perform a TCP scan on a list of ports for a given IP.
    Returns a list of open ports.
    """
    open_ports = []
    for port in target_ports:
        tcp_syn = scapy.IP(dst=target_ip) / scapy.TCP(dport=port, flags="S")
        response = scapy.sr1(tcp_syn, timeout=1, verbose=False)

        if response and response.haslayer(scapy.TCP) and response.getlayer(scapy.TCP).flags == 18:
            open_ports.append(port)
    
    return open_ports


def udp_scan(target_ip, target_ports):
    """
    Perform a UDP scan on a list of ports for a given IP.
    Returns a list of open ports.
    """
    open_ports = []
    for port in target_ports:
        udp_packet = scapy.IP(dst=target_ip) / scapy.UDP(dport=port)
        response = scapy.sr1(udp_packet, timeout=1, verbose=False)

        if response is None: # No response means that the port is open (common for UDP)
            open_ports.append(port)
    
    return open_ports