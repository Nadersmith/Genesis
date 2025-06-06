# genesis.py

from core.core import GenesisCore

if __name__ == "__main__":
    print("🔰 Welcome to GENESIS - The Final Defense 🔰")

    core = GenesisCore()
    core.load_module("scanner")
    core.load_module("watcher")
    core.load_module("reaper")

    core.run_all()
