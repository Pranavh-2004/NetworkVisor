import scapy.all as scapy

def ping_sweep(target_ip):
    """
    Perform a Ping Sweep on a given IP range or a single IP.
    Returns a list of live hosts that respond to ICMP Echo Requests.
    """
    icmp_request = scapy.ICMP() # ICMP Echo request (aka 'Ping')
    ip_request = scapy.IP(dst=target_ip)
    packet = ip_request / icmp_request # Combine IP and ICMP
    response_list = scapy.sr1(packet, timeout=1, verbose=False) # Send packet and wait for response

    live_hosts = []
    if response_list:
        live_hosts.append(target_ip)

    return live_hosts