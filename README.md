# IP-Network-Checker

## Introduction
This Python script efficiently checks if two given IP addresses belong to the same network based on their classes. It's a handy tool for network administrators and developers who need to verify network configurations and connections.


## User Instructions
To utilize this script, follow these steps:

1. **Run the script:**
   ```bash
   python3 ip_network_checker.py
2. **Enter the first IP address when prompted.**
3. **Enter the second IP address when prompted.**
4. **The script will output whether the given IP addresses are in the same network or not.**

## Functionality
The script includes the following functions:

check_same_network(ip1, ip2): This function takes two IP addresses as input and returns True if they belong to the same network, otherwise False.
get_ip_class(first_octet): This function determines the class of an IP address based on the first octet.

## Network Classes
In IPv4, IP addresses are divided into classes based on the first octet:

Class A: The first octet ranges from 1 to 126.
Class B: The first octet ranges from 128 to 191.
Class C: The first octet ranges from 192 to 223.
Class D: The first octet ranges from 224 to 239.
Class E: The first octet ranges from 240 to 247.

## Note
The script currently only supports IPv4 addresses.
Ensure that the input format for IP addresses is valid (e.g., "xxx.xxx.xxx.xxx").
