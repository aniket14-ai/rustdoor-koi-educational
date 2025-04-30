# RustDoor & Koi Stealer Simulation (Educational)

This repository provides an **educational simulation** of two malware variants inspired by real-world macOS threats:

- **RustDoor**: A backdoor built with Rust, simulating command execution and persistence via LaunchAgents.
- **Koi Stealer**: A Python script mimicking data collection from crypto wallets and browsers.

## 🚨 Disclaimer

> This project is strictly for educational and awareness purposes. It does **not** contain real malware, does **not** exfiltrate any data, and should **never** be used for malicious purposes. Please follow ethical hacking guidelines.

## 📦 Contents

- `rustdoor_demo/`: Rust-based fake backdoor with LaunchAgent persistence.
- `koi_stealer_mock/`: Python-based mock stealer demonstrating fake wallet & browser data exfiltration.

## 🛠️ Setup

### RustDoor

```bash
cd rustdoor_demo
cargo build
./target/debug/rustdoor_demo
