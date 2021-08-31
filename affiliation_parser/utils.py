import os
import shutil
import requests
import zipfile
import io
from pathlib import Path


def download_grid_data(
    url: str = "https://figshare.com/ndownloader/files/30589659",
    file_name: str = "grid",
):
    """
    Download GRID data from https://grid.ac/downloads
    to home directory "~/.affiliation_parser/grid"
    """
    path = Path(os.getenv("~", "~/.affliation_parser")).expanduser()
    grid_path = path / f"{file_name}"
    if not grid_path.exists():
        print(f"Downloading GRID dataset to {grid_path}.")
        grid_path.mkdir(parents=True, exist_ok=True)
        # download from url
        r = requests.get(url)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall(grid_path)
    else:
        print(f"You already downloaded GRID dataset to {grid_path}.")
