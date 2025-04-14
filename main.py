import argparse
import datetime
from core import (
    subdomains, whois_lookup, scanner, headers,
    dns_records, tech_stack, dirbuster, shodan_lookup, passive_recon,
    cve_scanner, email_harvester, social_profiles,
    favicon_hash, historical_dns, asn_scanner,
    report_gen
)

banner = """███████╗ ██████╗███████╗ ██████╗ ███████╗ █████╗ ███╗   ███╗
██╔════╝██╔════╝██╔════╝██╔═══██╗██╔════╝██╔══██╗████╗ ████║
█████╗  ██║     █████╗  ██║   ██║███████╗███████║██╔████╔██║
██╔══╝  ██║     ██╔══╝  ██║   ██║╚════██║██╔══██║██║╚██╔╝██║
███████╗╚██████╗██║     ╚██████╔╝███████║██║  ██║██║ ╚═╝ ██║
╚══════╝ ╚═════╝╚═╝      ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
              PWNED BY BackdoorAli aka NotAlita
                Red Team Recon Toolkit v1.0
"""

def main():
    parser = argparse.ArgumentParser(description='Red Team Recon Toolkit')
    parser.add_argument('target', help='Target domain or IP')
    parser.add_argument('--mode', choices=['stealth', 'aggressive'], default='stealth', help='Recon mode')
    parser.add_argument('--all', action='store_true', help='Run all recon modules for selected mode')
    parser.add_argument('--whois', action='store_true')
    parser.add_argument('--subdomains', action='store_true')
    parser.add_argument('--dns', action='store_true')
    parser.add_argument('--scan', action='store_true')
    parser.add_argument('--headers', action='store_true')
    parser.add_argument('--tech', action='store_true')
    parser.add_argument('--shodan', action='store_true')
    parser.add_argument('--passive', action='store_true')
    parser.add_argument('--dirbuster', action='store_true')
    parser.add_argument('--cve', action='store_true')
    parser.add_argument('--email', action='store_true')
    parser.add_argument('--social', action='store_true')
    parser.add_argument('--favicon', action='store_true')
    parser.add_argument('--histdns', action='store_true')
    parser.add_argument('--asn', action='store_true')
    parser.add_argument('--wordlist', help='Path to wordlist (for subdomain or dirbuster)')
    args = parser.parse_args()

    print(banner)
    print(f"[+] Target: {args.target}")
    print(f"[+] Mode: {args.mode}\n")

    report = {}

    if args.mode == 'stealth':
        if args.all or args.passive:
            report['Passive Recon'] = capture(passive_recon.run, args.target)
        if args.all or args.whois:
            report['WHOIS Lookup'] = capture(whois_lookup.run, args.target)
        if args.all or args.headers:
            report['HTTP Headers'] = capture(headers.run, args.target)
        if args.subdomains:
            report['Subdomains (Passive)'] = capture(passive_recon.run, args.target)

    if args.mode == 'aggressive':
        if args.all or args.dns:
            report['DNS Records'] = capture(dns_records.run, args.target)
        if args.all or args.subdomains:
            report['Subdomains'] = capture(subdomains.run, args.target, args.wordlist)
        if args.all or args.scan:
            report['Port Scan'] = capture(scanner.run, args.target)
        if args.all or args.tech:
            report['Tech Stack'] = capture(tech_stack.run, args.target)
        if args.all or args.shodan:
            report['Shodan Lookup'] = capture(shodan_lookup.run, args.target)
        if args.all or args.dirbuster:
            report['DirBuster'] = capture(dirbuster.run, args.target, args.wordlist)
        if args.whois:
            report['WHOIS Lookup'] = capture(whois_lookup.run, args.target)
        if args.headers:
            report['HTTP Headers'] = capture(headers.run, args.target)
        if args.passive:
            report['Passive Recon'] = capture(passive_recon.run, args.target)

    if args.cve:
        report['CVE Scanner'] = capture(cve_scanner.run, args.target)
    if args.email:
        report['Email Harvester'] = capture(email_harvester.run, args.target)
    if args.social:
        report['Social Profile Enumerator'] = capture(social_profiles.run, args.target)
    if args.favicon:
        report['Favicon Hash'] = capture(favicon_hash.run, args.target)
    if args.histdns:
        report['Historical DNS'] = capture(historical_dns.run, args.target)
    if args.asn:
        report['ASN Scanner'] = capture(asn_scanner.run, args.target)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    html_path = f"reports/recon_{timestamp}.html"
    pdf_path = f"reports/recon_{timestamp}.pdf"
    report_gen.run(report, html_path, pdf_path)
    report_gen.export_pdf(report, pdf_path)

def capture(func, *args):
    import io, sys
    buf = io.StringIO()
    sys_stdout = sys.stdout
    sys.stdout = buf
    try:
        func(*args)
    except Exception as e:
        print(f"[!] Error: {e}")
    sys.stdout = sys_stdout
    return buf.getvalue()

if __name__ == '__main__':
    main()
