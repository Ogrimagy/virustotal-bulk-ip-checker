# VirusTotal Bulk IP Checker

This script checks a list of IP addresses against VirusTotal's reputation database using the API v3.

## Usage
1. Get a [VirusTotal API key](https://www.virustotal.com/gui/my-apikey).
2. Put your IPs in `ips.txt`.
3. Run the script:
   ```bash
   python vt_bulk_ip.py
4. output example:
   8.8.8.8 → {'harmless': 85, 'malicious': 0, 'suspicious': 0, 'undetected': 5}
