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
