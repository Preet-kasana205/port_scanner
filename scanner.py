import socket

def scan_port(target, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1) # we can set a timeout for the connection attempt for faster scanning 0.5 seconds or 1 second is usually good for most cases
    result = scanner.connect_ex((target, port))
    scanner.close()
    if result == 0:
        return True
    else:
        return False

def main():
    target_name = input("Enter target : ")
    target = socket.gethostbyname(target_name)

    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    print(f"\nScanning {target_name} ({target})...")
    print(f"Scanning ports {start_port} to {end_port}")
    print("-" * 40)

    open_ports = []

    for port in range(start_port, end_port + 1):
        if scan_port(target, port):
            print(f"Port {port} is OPEN ✅")
            open_ports.append(port)

    print("-" * 40)
    print(f"Scan complete! Found {len(open_ports)} open ports.")

main()
