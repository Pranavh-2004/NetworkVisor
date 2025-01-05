# NetworkVisor

NetworkVisor is a powerful and flexible network scanning tool designed to help users perform ARP scans, port scans, and ping sweeps to assess the status of devices and services on a network. This tool is designed for educational purposes and legitimate network security assessments with proper permissions.

## Features

- **ARP Scan**: Discover devices in the local network using ARP requests and retrieve their IP and MAC addresses.
- **Port Scan**: Perform TCP and UDP port scans to identify open ports and services running on remote systems.
- **Ping Sweep**: Perform a ping sweep to check which hosts are live on the network.

## Disclaimer

By using this tool, you agree that you are solely responsible for the actions performed with it. This tool is intended solely for educational purposes and legitimate network security assessments within the bounds of applicable laws and regulations.

You must ensure that you have explicit permission from the network owner before scanning any network or system. Unauthorized scanning or network probing may be illegal in some countries and could result in legal consequences.

The creators and contributors of this project assume no responsibility for any misuse or damages resulting from the use of this tool.

## Installation

### Prerequisites

Make sure you have Python 3.6 or higher installed. Additionally, you will need to install the requirements file.

### Setting Up a Virtual Environment

To set up the project in a virtual environment, follow these steps:

1. Create a virtual environment:

```bash
python3 -m venv .venv
```

2. Activate the virtual environment:

- On macOS/Linux:

```bash
source .venv/bin/activate
```

- On Windows:

```bash
.venv\Scripts\activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Running NetworkVisor

To run NetworkVisor, use the following command structure:

```bash
python scripts/scanner.py -i <TARGET_IP> -t <SCAN_TYPE> [-p <PORTS>]
```

- -i <TARGET_IP>: The target IP or IP range for the scan (e.g., 192.168.1.1/24).
- -t <SCAN_TYPE>: The type of scan to perform (arp, ping, or port).
- -p <PORTS>: A comma-separated list of ports (only for port scan). For example, 80,443,22.

### Example Commands

1. Perform ARP scan:

```bash
python scripts/scanner.py -i 192.168.1.1/24 -t arp
```

2. Perform Ping sweep:

```bash
python scripts/scanner.py -i 192.168.1.1/24 -t ping
```

3. Perform TCP port scan:

```bash
python scripts/scanner.py -i 192.168.1.1 -t port -p 80,443,22
```

## Contributing

We welcome contributions to NetworkVisor! If you have an idea for an improvement or have found a bug, feel free to fork the repository, create a branch, and submit a pull request.

### Steps to Contribute:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Make your changes.
4. Write tests to verify your changes (if applicable).
5. Submit a pull request with a detailed description of the changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This project utilizes the Scapy library for network packet crafting and sniffing.
- Thanks to the open-source community for their contributions to network security tools.
