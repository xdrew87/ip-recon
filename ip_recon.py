import argparse
import requests
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from datetime import datetime

# ASCII Art Banner (cyber look)
BANNER = r"""
               _._
           __.{,_.}.__
        .-"           "-.
      .'  __.........__  '.
     /.-'`___.......___`'-.\ 
    /_.-'` /   \ /   \ `'-._\
    |     |   '/ \'   |     |
    |      '-'     '-'      |
    ;                       ;
    _\         ___         /_
   /  '.'-.__  ___  __.-'.'  \
 _/_    `'-..._____...-'`    _\_
/   \           .           /   \
\____)         .           (____/
    \___________.___________/
      \___________________/
     (_____________________)
[bold magenta]IP RECON[/bold magenta]
"""

SUBTITLE = (
    "[bold cyan]Cyberstyle IP Intelligence Tool[/bold cyan]\n"
    "[bright_black]by xdrew87[/bright_black]"
)

FOOTER = "[bold magenta]Made with [bold yellow]Python[/bold yellow] + [bold cyan]Rich[/bold cyan] | [bold green]Share your results![/bold green] | [bold white]github.com/xdrew87[/bold white]"

# Known hosting/cloud providers
HOSTING_PROVIDERS = [
    "amazon", "aws", "google", "azure", "ovh", "digitalocean", "linode",
    "hetzner", "contabo", "vultr", "oracle", "alibaba", "rackspace", "dreamhost",
    "gcp", "microsoft", "cloud", "server", "hosting"
]

def detect_ip_type(isp, org):
    combined = f"{isp} {org}".lower()
    for provider in HOSTING_PROVIDERS:
        if provider in combined:
            return "[bold magenta]Static (Server)[/bold magenta]"
    return "[bold green]Likely Dynamic (Residential ISP)[/bold green]"

def fetch_ip_info(ip):
    url = f"http://ip-api.com/json/{ip}"
    resp = requests.get(url, timeout=10)
    data = resp.json()
    return data

def main():
    parser = argparse.ArgumentParser(description="IP Recon: Hacker-style IP info tool")
    parser.add_argument("-i", "--ip", required=True, help="IP address to scan")
    parser.add_argument("--log", action="store_true", help="Save results to results.log")
    args = parser.parse_args()

    console = Console()
    # Banner panel with border
    console.print(Panel(Text.from_markup(BANNER, style="magenta"), border_style="cyan", padding=(1,2)))
    # Subtitle panel (centered, improved spacing)
    console.print(Panel(Text.from_markup(SUBTITLE, justify="center"), border_style="magenta", padding=(1,4)))
    console.print()  # Spacer

    try:
        data = fetch_ip_info(args.ip)
    except Exception as e:
        console.print(f"[bold red]Error fetching IP info: {e}[/bold red]")
        return

    if data.get("status") != "success":
        console.print(f"[bold red]API Error: {data.get('message', 'Unknown error')}[/bold red]")
        return

    ip_type = detect_ip_type(data.get("isp", ""), data.get("org", ""))

    table = Table(
        title=Text(f"IP Recon Results for {args.ip}", style="bold cyan"),
        style="white",
        border_style="magenta",
        padding=(0,1)
    )
    table.add_column("Field", style="bold green", justify="right")
    table.add_column("Value", style="bold yellow", justify="left")

    table.add_row("Country", Text(data.get('country', 'N/A'), style="bold yellow"))
    table.add_row("Region", Text(data.get("regionName", "N/A"), style="yellow"))
    table.add_row("City", Text(data.get("city", "N/A"), style="yellow"))
    table.add_row("ISP", Text(data.get("isp", "N/A"), style="bright_cyan"))
    table.add_row("Org", Text(data.get("org", "N/A"), style="bright_cyan"))
    table.add_row("ASN", Text(data.get("as", "N/A"), style="bright_magenta"))
    # Render ip_type markup
    table.add_row("IP Type", Text.from_markup(ip_type))

    console.print(table)
    console.print()  # Spacer
    # Footer panel (fix: use Text.from_markup for markup rendering)
    console.print(Panel(Text.from_markup(FOOTER, justify="center"), border_style="cyan", padding=(0,2)))

    if args.log:
        with open("results.log", "a", encoding="utf-8") as f:
            f.write(f"--- IP Recon {datetime.now()} ---\n")
            f.write(f"IP: {args.ip}\n")
            f.write(f"Country: {data.get('country', 'N/A')}\n")
            f.write(f"Region: {data.get('regionName', 'N/A')}\n")
            f.write(f"City: {data.get('city', 'N/A')}\n")
            f.write(f"ISP: {data.get('isp', 'N/A')}\n")
            f.write(f"Org: {data.get('org', 'N/A')}\n")
            f.write(f"ASN: {data.get('as', 'N/A')}\n")
            f.write(f"IP Type: {Text.from_markup(ip_type).plain}\n\n")

if __name__ == "__main__":
    main()
