import requests

API_KEY = "YOUR_API_KEY"   # Replace with your VirusTotal API key
headers = {"x-apikey": API_KEY}

def check_ips(file_path):
    with open(file_path) as f:
        ips = [line.strip() for line in f if line.strip()]

    for ip in ips:
        url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            stats = data["data"]["attributes"]["last_analysis_stats"]
            print(f"{ip} → {stats}")
        else:
            print(f"{ip} → Error {response.status_code}")

if __name__ == "__main__":
    check_ips("ips.txt")
