# utils/logger.py

import logging

def setup_logger():
    logger = logging.getLogger("Genesis")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        ch = logging.StreamHandler()
        ch.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s'))
        logger.addHandler(ch)
    return logger
