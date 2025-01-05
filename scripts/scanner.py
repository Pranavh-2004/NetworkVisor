import sys
import os

# Add project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import argparse
from scans.arp_scan import arp_scan
from scans.port_scan import tcp_scan, udp_scan
from scans.ping_sweep import ping_sweep
from prettytable import PrettyTable


def get_arguments():
    parser = argparse.ArgumentParser(description="Network Scanning Tool")
    parser.add_argument("-i", "--ip", dest="target", help="Target IP or IP Range", required=True)
    parser.add_argument("-t", "--type", dest="scan_type", choices=["arp", "ping", "port"], help="Type of scan to perform", required=True)
    parser.add_argument("-p", "--ports", dest="ports", help="Comma seperated list of ports for port scan", type=str)

    return parser.parse_args()

def print_table(coulumns, data):
    """
    Helper function to print the results in a formatted table.
    """
    table = PrettyTable()
    table.field_names = coulumns
    table.align = 'l' # Aligns columns to the left

    for row in data:
        table.add_row(row)

    print(table)


def main():
    options = get_arguments()

    if options.scan_type == "arp":
        print(f"Performing ARP scan on {options.target}...\n")
        devices = arp_scan(options.target)
        arp_data = [(device["ip"], device["mac"]) for device in devices]
        print_table(["IP Address, MAC Address"], arp_data)

    elif options.scan_type == "ping":
        print(f"Performing Ping sweep on {options.target}...\n")
        live_hosts = ping_sweep(options.target)
        ping_data = [(host,) for host in live_hosts]
        print_table(["Live Hosts"], ping_data)
    
    elif options.scan_type == "port":
        if not options.ports:
            print("[!] Please specify ports for port scan")
            return
        ports = [int(port) for port in options.ports.split(",")]
        print(f"Performing port scan on {options.target} for ports {', '.join(map(str, ports))}...\n")
        open_tcp_ports = tcp_scan(options.target, ports)
        open_udp_ports = udp_scan(options.target, ports)

        port_data = [
            ("Open TCP Ports", ",".join(map(str, open_tcp_ports))),
            ("Open UDP Ports", ",".join(map(str, open_udp_ports)))
        ]
        print_table(["Port Type", "Open Ports"], port_data)

if __name__ == "__main__":
    main()