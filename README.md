# 🛡️ VirusTotal Bulk IP Checker

A simple Python script for **SOC analysts** and **incident responders** to efficiently check a bulk list of IP addresses against the **VirusTotal API v3**. It's ideal for quickly identifying malicious indicators from logs or network captures.

-----

## 🚀 Getting Started

### 1\. **Setup**

  - **Clone the repository:**
    ```bash
    git clone https://github.com/ogrimagy/virustotal-ip-reputation.git
    cd virustotal-ip-reputation
    ```
  - **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
  - **Configure your API key:**
      - Get your free **VirusTotal API key** by signing up on their website.
      - Open `vt_bulk_ip.py` and replace `API_KEY` with your personal key.

-----

### 2\. **Create the Input File**

  - Create a file named **`ips.txt`** in the project directory.
  - Add the IP addresses you want to check, with one IP per line. For example:
    ```
    185.220.101.23
    104.244.42.1
    8.8.8.8
    ```

-----

### 3\. **Run the Script**

  - Execute the script from your terminal:
    ```bash
    python vt_bulk_ip.py
    ```
  - The output will display the reputation of each IP, showing the number of vendors that flagged it as `malicious`, `suspicious`, `harmless`, or `undetected`.
    ```
    185.220.101.23 → {'harmless': 60, 'malicious': 12, 'suspicious': 2, 'undetected': 8}
    104.244.42.1   → {'harmless': 85, 'malicious': 0, 'suspicious': 0, 'undetected': 5}
    8.8.8.8        → {'harmless': 90, 'malicious': 0, 'suspicious': 0, 'undetected': 0}
    ```

-----

## 🔄 Recommended Workflow

This script works great in a **cybersecurity workflow** for threat hunting and incident response:

1.  **Extract IPs:** Use tools like **Wireshark** (via `Statistics → Conversations → IPv4 → Copy → As CSV`) or log parsers to gather a list of IP addresses from network traffic.
2.  **Clean & Deduplicate:** Paste the raw list into **CyberChef** and use the **"Extract IP addresses"** and **"Remove duplicates"** operations to prepare a clean list.
3.  **Check Reputation:** Save the clean list to `ips.txt` and run this script to quickly identify malicious IPs for further investigation.

-----

## 📚 Technical Details

  - **`vt_bulk_ip.py`**: The main Python script that handles the API requests.
  - **`ips.txt`**: The input file for the IP addresses.
  - **`requirements.txt`**: Lists dependencies, primarily the `requests` library.

-----

## ⚠️ Important Note

  - Free VirusTotal API keys have rate limits (e.g., **4 requests/minute**). Be mindful of this when querying large lists of IPs to avoid hitting the API limit.
  - This tool is open-source and provided for **educational purposes** and **professional use** in security operations and threat hunting.

-----

## 📝 License

This project is licensed under the MIT License.
