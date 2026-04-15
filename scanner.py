import socket
from datetime import datetime

def scan_port(target, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1) # we can set a timeout for the connection attempt for faster scanning 0.5 seconds or 1 second is usually good for most cases
    result = scanner.connect_ex((target, port))
    scanner.close()
    if result == 0:
        return True
    else:
        return False
    
def save_results(target_name, target_ip, start_port, end_port, open_ports):
    filename  = f"results/scan_{target_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w") as file:
        file.write("=" * 40 + "\n")
        file.write(f"PORT SCANNER RESULTS\n")
        file.write("=" * 40 + "\n")
        file.write(f"Target: {target_name} ({target_ip})\n")
        file.write(f"Port Range: {start_port} to {end_port}\n")
        file.write(f"Scanner Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write("-" * 40 + "\n")

        if open_ports:
            file.write(f"Open Ports Found: {len(open_ports)}\n\n")
            for port in open_ports:
                file.write(f"  [OPEN] Port {port}\n")
        else:
            file.write("No open ports found.\n")

        file.write("\n" + "=" * 40 + "\n")
        file.write("Scan Complete.\n")

    print(f"\n📄 Results saved to: {filename}")

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
    
    save_results(target_name, target, start_port, end_port, open_ports)
main()
