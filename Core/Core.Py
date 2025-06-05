# core/core.py

import os
import importlib
import logging
from utils.logger import setup_logger

class GenesisCore:
    def __init__(self):
        self.logger = setup_logger()
        self.modules = {}

    def load_module(self, name):
        try:
            module_path = f"modules.{name}"
            module = importlib.import_module(module_path)
            self.modules[name] = module
            self.logger.info(f"✅ Loaded module: {name}")
        except Exception as e:
            self.logger.error(f"❌ Failed to load module {name}: {e}")

    def run_module(self, name):
        if name in self.modules:
            try:
                self.modules[name].run()
                self.logger.info(f"▶️ Ran module: {name}")
            except Exception as e:
                self.logger.error(f"❌ Error while running module {name}: {e}")
        else:
            self.logger.warning(f"⚠️ Module {name} not loaded.")

    def run_all(self):
        for name in self.modules:
            self.run_module(name)
