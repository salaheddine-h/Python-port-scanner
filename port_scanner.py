import socket
from datetime import datetime

# Target
target = input("Enter target IP or domain: ")

# Convert domain to IP
try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid target.")
    exit()

print("-" * 50)
print(f"Scanning target: {target_ip}")
print(f"Time started: {datetime.now()}")
print("-" * 50)

try:
    for port in range(1, 1025):  # Scan common ports
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        s.close()


except KeyboardInterrupt:
    print("\nScan interrupted.")
    exit()

