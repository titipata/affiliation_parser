import re

from ..data import UNIVERSITY_ABBR


def replace_institution_abbr(affil_text: str):
    """
    Replace abbreviation with full institution string
    """
    for university_list in UNIVERSITY_ABBR:
        for university in university_list:
            if university in affil_text:
                affil_text = re.sub(university, university_list[0], affil_text)
                return affil_text
    return affil_text


def clean_text(affil_text: str):
    """
    Given affiliation text with abbreviation, clean that text
    """
    affil_text = affil_text.strip()
    affil_text = re.sub("\t", " ", affil_text)
    affil_text = re.sub("Dept. ", "Department ", affil_text)
    affil_text = re.sub("Surg. ", "Sugery ", affil_text)
    affil_text = re.sub("Univ. ", "University ", affil_text)
    affil_text = affil_text[2:] if affil_text.startswith("2 ") else affil_text
    affil_text = affil_text[3:] if affil_text.startswith("2. ") else affil_text
    affil_text = re.sub(r"\*", " ", affil_text)
    affil_text = re.sub(";", "", affil_text)
    affil_text = re.sub("E-mail:", "", affil_text)
    affil_text = re.sub("email:", "", affil_text)
    affil_text = re.sub("P.O. Box", "", affil_text)
    affil_text = replace_institution_abbr(affil_text)
    return affil_text.strip()