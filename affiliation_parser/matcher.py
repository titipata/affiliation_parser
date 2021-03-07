import os
import re
import csv
from pathlib import Path
import subprocess

import pandas as pd
from nltk.tokenize import WhitespaceTokenizer

from .utils import download_grid_data
from .parse import parse_affil, preprocess


path = Path(os.getenv("~", '~/.affliation_parser')).expanduser()
grid_path = (path/"grid")
if not grid_path.exists():
    download_grid_data()


def match_affil(affiliation: str):
    """Match affliation to GRID dataset."""
    parsed_affil = parse_affil(affiliation)
    return None
