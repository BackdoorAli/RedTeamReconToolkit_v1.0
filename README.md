```
███████╗ ██████╗███████╗ ██████╗ ███████╗ █████╗ ███╗   ███╗
██╔════╝██╔════╝██╔════╝██╔═══██╗██╔════╝██╔══██╗████╗ ████║
█████╗  ██║     █████╗  ██║   ██║███████╗███████║██╔████╔██║
██╔══╝  ██║     ██╔══╝  ██║   ██║╚════██║██╔══██║██║╚██╔╝██║
███████╗╚██████╗██║     ╚██████╔╝███████║██║  ██║██║ ╚═╝ ██║
╚══════╝ ╚═════╝╚═╝      ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
    (Enumeration, Collection, Fingerprinting, Overview
               Scanning, Analysis, Mapping)   
            PWNED BY BackdoorAli aka NotAlita
               Red Team Recon Toolkit v1.0
```

## Overview

The **Red Team Recon Toolkit** is a personal cybersecurity recon suite designed and developed by **BackdoorAli aka NotAlita**. This project was built to demonstrate technical capabilities in offensive security, and is intended strictly for **educational, professional portfolio, and authorized use only**.

---

## Features

### Core Recon Modules
- Subdomain Enumeration (wordlist-based)
- DNS Record Dumping
- WHOIS Lookup
- HTTP Headers Check
- Technology Stack Fingerprinting

### Advanced Recon Modules
- Shodan Integration
- CVE Scanner (via NVD or Vuln API)
- Directory Buster
- Historical DNS Dump
- Email Harvester
- Social Profile Enumerator
- Favicon Hash Analyzer
- ASN & IP Range Scanner
- Passive Recon Toolkit

### CLI Capabilities
- Mode toggle: Stealth vs Aggressive
- Selective module execution or all-in-one batch
- Dynamic CLI interface with banners and organized menus

### Output & Reporting
- HTML + PDF reporting via report_gen.py
- Timestamped file outputs
- Per-module PDF export + full session summary

---

## Folder Structure

```
RedTeamReconToolkit_v1.0/
├── assets/
│   └── logo.txt
├── core/
│   ├── headers.py
│   ├── scanner.py
│   ├── subdomains.py
│   └── whois_lookup.py
├── modules/
│   ├── __init__.py
│   ├── advanced/
│   └── extras/
├── reports/
│   └── *.html / *.pdf
├── templates/
│   ├── base.html
│   └── report.html
├── utils/
│   ├── formatter.py
│   └── __init__.py
├── wordlists/
│   └── common.txt
├── main.py
├── README.md
├── LICENSE
└── requirements.txt
```

---

## Setup

```bash
pip install -r requirements.txt
```

---

## Usage

```bash
python main.py
```

- Choose Stealth or Aggressive mode
- Select individual modules or run all
- Results will be saved to /reports in both HTML and PDF format

---

## ⚠️ LICENSE & USAGE

This project is protected under a **custom Proprietary License**.  
You may **not copy, reuse, distribute, or integrate** this toolkit without the explicit, signed, and written permission of the author.

This toolkit is intended for:

- ✅ Personal, educational use
- ✅ Authorised testing environments
- ✅ Demonstration of capabilities during job applications

For any organisational or commercial use, please contact the author to request a formal license and usage agreement.

See the full legal terms in [LICENSE](LICENSE)

---

## Author

**BackdoorAli aka NotAlita**  
GitHub: [https://github.com/BackdoorAli](https://github.com/BackdoorAli)

---

## Contact for Licensing or Questions

Interested in hiring, licensing, or collaborative use?  
Reach out at: [https://github.com/BackdoorAli](https://github.com/BackdoorAli)

Last updated: July 24, 2025
