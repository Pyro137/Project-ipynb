import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, 
                    format="[%(asctime)s:  %(levelname)s]:%(message)s ")

while True:
    projects_name=input("Project Name:")
    if projects_name!="":
        break
logging.info(f"creating project by name: {projects_name}")

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{projects_name}/__init__.py",
    "init_setup.sh",
    "reqirements.txt",
    "reqirements_dev.txt",
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini",
]

for filepath in list_of_files:
    file_path=Path(filepath)
    file_dir,file_name=os.path.split(file_path)
    if file_dir!="":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"creating directory: {file_dir}")
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path, "w") as f:
            pass
        logging.info(f"creating file: {file_name} in {file_path}")