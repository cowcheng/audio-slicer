import logging
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]

LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_DATEFMT = "%Y-%m-%d %H:%M:%S"
LOG_LEVEL = logging.INFO
