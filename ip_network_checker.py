def check_same_network(ip1, ip2):
    ip1_parts = ip1.split('.')
    ip2_parts = ip2.split('.')
    # Check if IPs are of the same version (IPv4)
    if len(ip1_parts) != 4 or len(ip2_parts) != 4:
        return False
    
    # Check IP classes
    ip1_class = get_ip_class(ip1_parts[0])
    ip2_class = get_ip_class(ip2_parts[0])

    if ip1_class != ip2_class:
        return False
    # Check if IPs are in the same network based on their classes

    match ip1_class:
        case 'A':
            return ip1_parts[0] == ip2_parts[0]
        case 'B':
            return ip1_parts[0] == ip2_parts[0] and ip1_parts[1] == ip2_parts[1]
        case 'C':
            return ip1_parts[0] == ip2_parts[0] and ip1_parts[1] == ip2_parts[1] and ip1_parts[2] == ip2_parts[2]            
        case _:
            return False

def get_ip_class(first_octet):
    first_octet = int(first_octet)
    if 0 <= first_octet <= 126:
        return 'A'
    elif 128 <= first_octet <= 191:
        return 'B'
    elif 192 <= first_octet <= 255:
        return 'C'
    else:
        return 'Unknown'

# Input IP addresses from the user
ip1 = input("Enter the first IP address: ")
ip2 = input("Enter the second IP address: ")

# Check if IPs are in the same network
if check_same_network(ip1, ip2):
    print("IPs are in the same network")
else:
    print("IPs are not in the same network")
