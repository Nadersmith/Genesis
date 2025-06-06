# genesis.py

from core.core import GenesisCore

def print_genesis_banner():
    banner = r'''
  ██████╗ ███████╗███╗   ██╗███████╗██╗███████╗███████╗
 ██╔════╝ ██╔════╝████╗  ██║██╔════╝██║██╔════╝██╔════╝
 ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██║█████╗  ███████╗
 ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██║██╔══╝  ╚════██║
 ╚██████╔╝███████╗██║ ╚████║██║     ██║███████╗███████║
  ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═╝     ╚═╝╚══════╝╚══════╝

             GENESIS — The Final Defense 🔰
    '''
    print(banner)

if __name__ == "__main__":
    print_genesis_banner()

    core = GenesisCore()
    core.load_module("scanner")
    core.load_module("watcher")
    core.load_module("reaper")

    core.run_all() 
