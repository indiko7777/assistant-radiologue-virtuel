"""Télécharge le Processed RSNA Pneumonia Detection Dataset depuis Kaggle
et le copie dans data/rsna_pneumonia/.

Prérequis :
- pip install kagglehub
- Un jeton API Kaggle valide : ~/.kaggle/kaggle.json
  ou les variables d'environnement KAGGLE_USERNAME / KAGGLE_KEY.
"""

import shutil
from pathlib import Path

import kagglehub

DATASET_SLUG = "iamtapendu/rsna-pneumonia-processed-dataset"
DEST_DIR = Path(__file__).parent / "rsna_pneumonia"


def main() -> None:
    cache_path = Path(kagglehub.dataset_download(DATASET_SLUG))
    print("Dataset téléchargé dans le cache kagglehub :", cache_path)

    DEST_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copytree(cache_path, DEST_DIR, dirs_exist_ok=True)
    print("Dataset copié dans :", DEST_DIR)


if __name__ == "__main__":
    main()