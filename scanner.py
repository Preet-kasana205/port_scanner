import socket

def scan_port(target, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    result = scanner.connect_ex((target, port))
    scanner.close()

    if result == 0:
        print(f"Port {port} is OPEN ✅")
    else:
        print(f"Port {port} is CLOSED ❌")

target = socket.gethostbyname("google.com")
scan_port(target, 80)
scan_port(target, 443)
scan_port(target, 9999)
