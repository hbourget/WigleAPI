# Wigle Location Finder

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.7%2B-purple.svg)

## Prerequisites

- Python 3.7 or higher
- A WiGLE API key (register on [wigle.net](https://wigle.net/))

## Installation

1. **Clone the repository**

   ```bash
   https://github.com/hbourget/WigleAPI.git
   cd WigleAPI
   ```

2. **Create a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the script**

   ```bash
   python main.py --country CH --ssid "ExampleSSID" --bssid "00:14:22:01:23:45"
   ```

   - Replace `<COUNTRY_CODE>` with the desired country code (e.g., FR, CH, BE).
   - Replace `<SSID_NAME>` with the Wi-Fi network name you want to query.
   - Replace `<BSSID_ADDRESS>` with the Wi-Fi access point MAC address.

## License

This project is licensed under the [MIT License](LICENSE).
