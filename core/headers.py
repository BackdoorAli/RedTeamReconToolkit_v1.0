import requests

def run(domain):
    print(f"[Headers] Retrieving HTTP headers for {domain}\n")
    try:
        r = requests.get(f"http://{domain}", timeout=5)
        for header, value in r.headers.items():
            print(f"{header}: {value}")
    except Exception as e:
        print(f"[-] Failed to fetch headers: {e}")
