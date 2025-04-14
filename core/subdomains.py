import requests

def run(domain, wordlist_path=None):
    print(f"[Subdomains] Enumerating subdomains for {domain}\n")
    wordlist = ["www", "mail", "ftp", "test", "dev", "portal"]
    if wordlist_path:
        try:
            with open(wordlist_path, 'r') as f:
                wordlist = [line.strip() for line in f]
        except:
            print("[-] Failed to read wordlist, using default")

    for sub in wordlist:
        url = f"http://{sub}.{domain}"
        try:
            r = requests.get(url, timeout=2)
            if r.status_code < 400:
                print(f"[+] Found: {url}")
        except:
            continue
