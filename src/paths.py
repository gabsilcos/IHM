from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT = Path(os.getenv("PROJECT_ROOT", ".")).resolve().parents[0]

DATA_DIR = PROJECT_ROOT / os.getenv("DATA_DIR", "data")
RAW_DATA_DIR = PROJECT_ROOT / os.getenv("RAW_DATA_DIR", "data/raw")
PROCESSED_DATA_DIR = PROJECT_ROOT / os.getenv("PROCESSED_DATA_DIR", "data/processed")

REPORTS_DIR = PROJECT_ROOT / os.getenv("REPORTS_DIR", "reports")
FIGURES_DIR = PROJECT_ROOT / os.getenv("FIGURES_DIR", "reports/figures")

OUTPUTS_DIR = PROJECT_ROOT / os.getenv("OUTPUTS_DIR", "outputs")
MODELS_DIR = OUTPUTS_DIR / "models"
METRICS_DIR = OUTPUTS_DIR / "metrics"

ALL_DIRS = [
    DATA_DIR,
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    REPORTS_DIR,
    FIGURES_DIR,
    OUTPUTS_DIR,
    MODELS_DIR,
    METRICS_DIR,
]


def create_project_structure():
    """Cria todas as pastas se elas não existirem."""
    for directory in ALL_DIRS:
        directory.mkdir(parents=True, exist_ok=True)