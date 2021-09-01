import os
from pathlib import Path
from typing import Optional, Union
import numpy as np
import pandas as pd

import recordlinkage
from recordlinkage.index import Full

from .utils import download_grid_data
from .parse import parse_affil

path = Path(os.getenv("~", "~/.affliation_parser")).expanduser()
grid_path = path / "grid"
if not grid_path.exists():
    download_grid_data()  # if GRID data does not exist, download it locally
grid_df = pd.read_csv(
    grid_path / "grid.csv",
    header=0,
    names=["grid_id", "institution", "city", "state", "country"],
)
grid_df[
    "location"] = grid_df.city + " " + grid_df.state  # adding location column


def match_affil(affiliation: Optional[Union[str, list]], k: int = 3):
    """
    Match a given affliation string to GRID dataset.
    Return a list of most probable match as output from GRID dataset with GRID ids.

    We perform an affiliation parser to institution, location, and country
    before matching to GRID dataset. An additional text normalization
    to the GRID format will help improve the accuracy of the matching.
    For example, US or USA -> United States.

    affiliation: str, affiliation string
    k: int, number of output matches
    """
    if isinstance(affiliation, str):
        parsed_affil = parse_affil(affiliation)
        df = pd.DataFrame([parsed_affil])
    elif isinstance(affiliation, list):
        parsed_affils = [parse_affil(a) for a in affiliation]
        df = pd.DataFrame(parsed_affils)
    else:
        return None

    indexer = recordlinkage.Index()
    indexer.add(Full())
    candidate_links = indexer.index(df, grid_df)

    # recordlinkage comparer
    compare = recordlinkage.Compare()
    compare.string("institution", "institution", method="jarowinkler")
    compare.string("location", "location", method="jarowinkler")
    compare.string("country", "country", method="jarowinkler")

    features_df = compare.compute(candidate_links, df, grid_df)
    features_df["score"] = np.average(features_df,
                                      axis=1,
                                      weights=[0.6, 0.2, 0.2])

    if isinstance(affiliation, str):
        # return a list of top-k closest match
        topk_df = (features_df[["score"]].reset_index().sort_values(
            "score", ascending=False).head(k))
        topk_df = topk_df.merge(grid_df.reset_index(),
                                left_on="level_1",
                                right_on="index").drop(
                                    labels=["level_0", "level_1", "location"],
                                    axis=1)
        return topk_df.to_dict(orient="records")

    elif isinstance(affiliation, list):
        # return a list of list of top-k closest match
        topk_list = []
        for _, topk_df in features_df.reset_index().groupby("level_0"):
            topk_df = (features_df[["score"]].reset_index().sort_values(
                "score", ascending=False).head(k))
            topk_df = topk_df.merge(grid_df.reset_index(),
                                    left_on="level_1",
                                    right_on="index").drop(labels=[
                                        "level_0", "level_1", "location"
                                    ],
                                                           axis=1)
            topk_list.append(topk_df.to_dict(orient="records"))
        return topk_list
    else:
        return None
