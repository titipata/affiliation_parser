import re


def clean_text(affil_text: str):
    """
    Given affiliation text with abbreviation, clean that text
    """
    affil_text = affil_text.strip()

    affil_text = re.sub("\t", " ", affil_text)
    affil_text = re.sub(r"\*", " ", affil_text)
    affil_text = re.sub(";", "", affil_text)

    affil_text = re.sub("Univ. ", "University ", affil_text)
    affil_text = re.sub("Dept. ", "Department ", affil_text)
    affil_text = re.sub("Surg. ", "Surgery ", affil_text)

    affil_text = re.sub("E-mail:", "", affil_text)
    affil_text = re.sub("email:", "", affil_text)
    affil_text = re.sub("P.O. Box", "", affil_text)  # zip code

    return affil_text.strip()