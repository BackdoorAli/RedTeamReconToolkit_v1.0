import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    try:
        with socket.create_connection((ip, port), timeout=2):
            print(f"[+] Port {port} is OPEN")
    except:
        pass

def run(target):
    print(f"[Scanner] Scanning ports on {target}\n")
    ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3306, 3389]
    with ThreadPoolExecutor(max_workers=20) as executor:
        for port in ports:
            executor.submit(scan_port, target, port)
