import re

import numpy as np
from unidecode import unidecode

from .parser import *


def parse_affil(affil_text):
    """
    Parse affiliation string to institution and department
    """
    affil_text = unidecode(affil_text)
    affil_text = clean_text(affil_text)
    email = parse_email(affil_text)
    zip_code = parse_zipcode(affil_text)
    affil_text = re.sub(email, "", affil_text)
    affil_text = re.sub(zip_code, "", affil_text)

    affil_list = affil_text.split(", ")
    affil = list()
    location = list()
    departments = list()

    for i, a in enumerate(affil_list):
        for ins in INSTITUTE:
            if ins in a.lower() and (not a in affil):
                affil.append(a)
                location = affil_list[i + 1::]

    # remove unwanted from affliation list and location list
    pop_index = list()
    for i, a in enumerate(affil):
        for rm in REMOVE_INSTITUE:
            if rm in a.lower() and (not "university" in a.lower()):
                pop_index.append(i)
    affil = np.delete(affil, list(set(pop_index))).tolist()

    pop_index = list()
    for i, l in enumerate(location):
        for rm in DEPARMENT:
            if rm in l.lower():
                pop_index.append(i)
    location = np.delete(location, list(set(pop_index))).tolist()

    affil = ", ".join(affil)
    location = ", ".join(location)
    if location == "":
        location = affil_text.split(", ")[-1]
    location = re.sub(r"\([^)]*\)", "", location).strip()

    for i, a in enumerate(affil_list):
        for dep in DEPARMENT:
            if dep in a.lower() and (not a in departments):
                departments.append(affil_list[i])
    department = ", ".join(departments)

    dict_location = parse_location(location)
    affil = append_institution_city(affil, dict_location["location"])

    dict_out = {
        "full_text": affil_text.strip(),
        "department": department.strip(),
        "institution": affil.strip(),
        "email": email,
        "zipcode": zip_code,
    }
    dict_out.update(dict_location)
    if dict_out["country"] == "":
        dict_out["country"] = check_country(affil_text)  # check country
    return dict_out
