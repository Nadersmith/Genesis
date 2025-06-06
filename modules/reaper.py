# modules/reaper.py

import psutil

def run():
    print("🧠 [reaper] Analyzing for suspicious behavior...")

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            cpu = proc.info['cpu_percent']
            mem = proc.info['memory_percent']
            if cpu > 40 or mem > 30:
                print(f"⚠️ High resource usage: {proc.info['name']} | CPU: {cpu}% | MEM: {mem:.2f}%")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    print("✅ Behavior analysis complete.")
