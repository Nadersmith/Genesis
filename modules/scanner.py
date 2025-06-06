# modules/scanner.py

import os

def run():
    print("🧪 [scanner] Running file scan...")

    suspicious_extensions = ['.exe', '.bat', '.vbs', '.scr', '.ps1', '.sh', '.dll']
    scan_path = '/home'  # عدل المسار حسب النظام

    threats = []

    for root, dirs, files in os.walk(scan_path):
        for file in files:
            filepath = os.path.join(root, file)
            ext = os.path.splitext(file)[1].lower()
            if ext in suspicious_extensions:
                print(f"⚠️ Suspicious file found: {filepath}")
                threats.append(filepath)

    print(f"✅ Scan complete. Total suspicious files: {len(threats)}")
