# modules/watcher.py

import psutil

def run():
    print("👁️ [watcher] Monitoring system processes and open ports...")

    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            print(f"🔍 Process: {proc.info['name']} (PID: {proc.info['pid']}) by {proc.info['username']}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    print("\n🌐 Open network connections:")
    for conn in psutil.net_connections():
        if conn.status == 'ESTABLISHED':
            print(f"🔌 Port {conn.laddr.port} <-> {conn.raddr.ip}:{conn.raddr.port} | PID: {conn.pid}")
