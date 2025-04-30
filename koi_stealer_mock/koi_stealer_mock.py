import json
import platform
import time

def mock_collect_data():
    print("[KoiStealer] Collecting fake browser and wallet data...")
    return {
        "os": platform.system(),
        "user": platform.node(),
        "wallets": ["FAKE_SEED_METAMASK", "FAKE_EXODUS_KEY"],
        "browser_cookies": ["FAKE_COOKIE1", "FAKE_COOKIE2"]
    }

def mock_exfiltrate(data):
    print("[KoiStealer] Simulating data exfiltration to C2...")
    print(json.dumps(data, indent=4))
    # No real exfiltration for educational safety.

def main():
    print("[KoiStealer] Educational simulation started.")
    time.sleep(1)
    data = mock_collect_data()
    mock_exfiltrate(data)

if __name__ == "__main__":
    main()
