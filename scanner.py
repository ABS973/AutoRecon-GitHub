import subprocess

target = "example.com"

def run_scan():
    result = subprocess.run(
        ["nmap", "-F", target],
        capture_output=True,
        text=True
    )
    return result.stdout

if __name__ == "__main__":
    output = run_scan()
    with open("scan_result.txt", "w") as f:
        f.write(output)
