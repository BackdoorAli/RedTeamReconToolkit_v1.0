import whois

def run(domain):
    print(f"[WHOIS] Performing WHOIS lookup for {domain}\n")
    try:
        w = whois.whois(domain)
        for key, value in w.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"[-] WHOIS lookup failed: {e}")
