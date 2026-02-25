import subprocess
import datetime
import argparse
from report_generator import generate_html_report
from colorama import Fore, Style, init

init(autoreset=True)

SAFE_TARGETS = ["scanme.nmap.org", "127.0.0.1", "localhost"]

def run_scan(target):
    print(Fore.GREEN + f"Scanning {target}...")
    result = subprocess.run(
        ["nmap", "-F", target],
        capture_output=True,
        text=True
    )
    return result.stdout

def save_report(data, target):
    filename = f"scan_report_{target}_{datetime.date.today()}.txt"
    with open(filename, "w") as f:
        f.write(data)
    print(Fore.BLUE + f"Text report saved as {filename}")
    return filename

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AutoRecon: Nmap Automation Tool")
    parser.add_argument("-t", "--target", required=True, help="Target domain or IP")
    args = parser.parse_args()

    if args.target not in SAFE_TARGETS:
        print(Fore.RED + "Target not allowed! Use a safe test target.")
        exit(1)

    output = run_scan(args.target)
    save_report(output, args.target)
    generate_html_report(output, args.target)