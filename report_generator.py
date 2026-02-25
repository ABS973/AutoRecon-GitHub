import datetime

def generate_html_report(scan_text, target):
    filename = f"scan_report_{target}_{datetime.date.today()}.html"
    html_content = f"""
    <html>
    <head><title>Scan Report: {target}</title></head>
    <body>
    <h1>Scan Report: {target}</h1>
    <pre>{scan_text}</pre>
    </body>
    </html>
    """
    with open(filename, "w") as f:
        f.write(html_content)
    print(f"HTML report saved as {filename}")
    return filename