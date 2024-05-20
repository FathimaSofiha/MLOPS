import os
from pathlib import Path
import logging

list_of_files=[
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"
]

# Configure logging to write to a file
logging.basicConfig(filename="file_organizer.log", filemode="a", format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()  # Create a logger object
logger.setLevel(logging.INFO)  # Set the logging level

def organize_files(list_of_files):
    """
    This function iterates through a list of files, creates necessary directories,
    and creates empty files if they don't exist, logging actions to a file.
    """
    for filepath in list_of_files:
        filepath = Path(filepath)  # Ensure filepath is a Path object
        filedir = filepath.parent  # Get the directory path directly

        # Create directory if it doesn't exist
        if not os.path.exists(filedir):
            os.makedirs(filedir, exist_ok=True)
            logger.info(f"Creating directory: {filedir}")

        # Create empty file if needed
        if not filepath.exists() or filepath.stat().st_size == 0:
            with open(filepath, "w") as f:
                pass  # Create empty file
            logger.info(f"Created file: {filepath}")

    logger.info("All files organized successfully!")

organize_files(list_of_files)