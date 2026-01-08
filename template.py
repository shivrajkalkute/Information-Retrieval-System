import os
from pathlib import Path
import logging

print("CURRENT WORKING DIRECTORY:", os.getcwd())  # 👈 ADD THIS

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s]: %(message)s'
)

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "app.py",
    "research/trials.ipynb",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir}")

    if not filepath.exists():
        with open(filepath, "w"):
            pass
        logging.info(f"Creating empty file: {filepath}")
