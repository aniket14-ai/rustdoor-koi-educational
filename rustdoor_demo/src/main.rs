use std::{fs, process::Command, thread, time::Duration};

fn setup_persistence() {
    let plist_content = format!(
        r#"
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.educational.rustdoor</string>
    <key>ProgramArguments</key>
    <array>
        <string>/Users/{}/rustdoor_demo/target/debug/rustdoor_demo</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
"#,
        whoami::username()
    );

    let plist_path = format!(
        "/Users/{}/Library/LaunchAgents/com.educational.rustdoor.plist",
        whoami::username()
    );

    fs::write(plist_path, plist_content).expect("Could not write plist for persistence.");
    println!("[RustDoor] Persistence plist written.");
}

fn simulate_command() {
    println!("[RustDoor] Running mock system command...");
    let output = Command::new("ls")
        .arg("-la")
        .output()
        .expect("Failed to run command");

    println!("{}", String::from_utf8_lossy(&output.stdout));
}

fn main() {
    setup_persistence();

    loop {
        println!("[RustDoor] Polling mock C2...");
        simulate_command();
        thread::sleep(Duration::from_secs(30));
    }
}
