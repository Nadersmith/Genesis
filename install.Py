# install.py

import subprocess
import sys
import os

def install_requirements():
    if not os.path.exists("requirements.txt"):
        print("❌ requirements.txt not found.")
        return

    print("📦 Installing required packages from requirements.txt...\n")

    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("\n✅ All packages installed successfully!")
    except subprocess.CalledProcessError as e:
        print("\n❌ Failed to install packages.")
        print(e)

if __name__ == "__main__":
    install_requirements()
