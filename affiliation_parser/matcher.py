import os
import re
import csv
import subprocess
from collections import namedtuple
from nltk.metrics.distance import jaccard_distance

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from sklearn.externals import joblib

from .parse import parse_affil, preprocess

Affiliation = namedtuple('Affiliation', ['name', 'country'])
REPO_DIR = os.path.join(os.path.expanduser('~'), 'affiliation_parser_data')
DATA_DIR = os.path.join(REPO_DIR, 'data')
MODEL_DIR = os.path.join(REPO_DIR, 'model')

def download_grid():
    """Download GRID dataset from S3 (last update: September 2016)"""
    subprocess.call(['wget', 'https://s3-us-west-2.amazonaws.com/science-of-science-bucket/grid/grid.csv',
                     '--directory', DATA_DIR])

def train_grid():
    """Train nearest neighbor model and save to model folder"""
    if not os.path.isfile(os.path.join(MODEL_DIR, 'nearest_neighbor.pkl')):
        print("download and save model to %s" % REPO_DIR)
        if not os.path.isdir(REPO_DIR):
            os.mkdir(REPO_DIR)
        if not os.path.isdir(MODEL_DIR):
            os.mkdir(MODEL_DIR)
        if not os.path.isdir(DATA_DIR):
            os.mkdir(DATA_DIR)
        if not os.path.isfile(os.path.join(DATA_DIR, 'grid.csv')):
            download_grid()
        grid_dict = list(csv.DictReader(open(os.path.join(DATA_DIR, 'grid.csv'), 'r')))

        grid_preprocess = []
        for g in grid_dict:
            grid_preprocess.append(preprocess(g['Name'] + ' ' + g['Country']))

        tfidf_model = TfidfVectorizer(min_df=3, max_df=0.8,
                                      lowercase=True, norm='l2',
                                      strip_accents='unicode',
                                      token_pattern=r'\w{1,}', ngram_range=(1,1),
                                      use_idf=True, smooth_idf=True, sublinear_tf=True,
                                      stop_words='english')

        X_grid = tfidf_model.fit_transform(grid_preprocess)
        nbrs_model  = NearestNeighbors(n_neighbors=1, algorithm='ball_tree',
                                       metric='minkowski', n_jobs=-1).fit(X_grid)
        joblib.dump(tfidf_model, os.path.join(MODEL_DIR, 'tfidf.pkl'))
        joblib.dump(nbrs_model, os.path.join(MODEL_DIR, 'nearest_neighbor.pkl'))

# train nearest neighbor model for GRID dataset
train_grid()
tfidf_model = joblib.load(os.path.join(MODEL_DIR, 'tfidf.pkl'))
nbrs_model = joblib.load(os.path.join(MODEL_DIR, 'nearest_neighbor.pkl'))

# distance function
def country_distance(affil_1, affil_2):
    """"""
    if affil_1.country == affil_2.country or affil_1.country == '' or affil_2.country == '':
        return 0
    else:
        return 1

def unigram_distance(affil_1, affil_2):
    """Unigram distance between two affiliation tuple"""
    affil_set_1 = set(w_tokenizer.tokenize(affil_1.name))
    affil_set_2 = set(w_tokenizer.tokenize(affil_2.name))
    overlap_len = len(affil_set_1.intersection(affil_set_2))
    dist = min(abs(len(affil_set_1) - overlap_len), abs(len(affil_set_2) - overlap_len))
    return dist

def jaccard_unigram_distance(affil_1, affil_2):
    """Unigram distance between two strings"""
    affil_set_1 = set(w_tokenizer.tokenize(affil_1.name))
    affil_set_2 = set(w_tokenizer.tokenize(affil_2.name))
    return jaccard_distance(affil_set_1, affil_set_2)

def affiliation_check(affil_1, affil_2):
    """
    Function to quickly check if both strings are the same
    if return 0 means both string are the same
    """
    if country_distance(affil_1, affil_2) == 0 and len(affil_2.name.split(" ")) >= 2:
        if unigram_distance(affil_1, affil_2) <= 1:
            dist = 0
        elif jaccard_unigram_distance(affil_1, affil_2) >= 0.75:
            dist = 0
        elif affil_1.name in affil_2.name or affil_2.name in affil_1.name:
            dist = 0
        else:
            dist = 1
    else:
        dist = 1
    return dist

def match_affil(affil_text):
    """
    Match affiliation string to GRID dataset
    the return GRID identification number
    """
    grid_dict = list(csv.DictReader(open(os.path.join(DATA_DIR, 'grid.csv'), 'r')))
    dict_affil = parse_affil(affil_text)
    institution = preprocess(dict_affil['institution'])
    country = preprocess(dict_affil['country'])
    affil = Affiliation(institution, country)
    tfidf_feature = tfidf_model.transform([institution + ' ' + country])
    distance, index = nbrs_model.kneighbors(tfidf_feature)
    i = index.ravel()[0]

    if distance <= 0.1:
        matched = True
    else:
        dist = affiliation_check(grid_data[i], affil)
        matched = True if dist == 0 else False

    if matched:
        return grid_dict[i]
    else:
        return None
