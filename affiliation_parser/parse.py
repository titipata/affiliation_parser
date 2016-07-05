import re
from unidecode import unidecode
from .keywords import *

def parse_location(location):
    zip_code_group = ''
    zip_code = re.search('(\d{5})([- ])?(\d{4})?', location)
    if zip_code is not None:
        zip_code_group = zip_code.groups()
        zip_code_group = [p for p in zip_code_group if p is not None][0]
    location = re.sub(zip_code_group, '', location)
    dict_location = {'location': location,
                     'zipcode': zip_code_group}
    return dict_location

def parse_affil(affil_text):
    """
    Parse affiliation string to institution and department
    """
    affil_text = unidecode(affil_text)
    affil_list = affil_text.split(', ')
    affil = ''
    department = ''
    location = ''
    for i, a in enumerate(affil_list):
        for ins in INSTITUTE:
            if ins in a.lower():
                affil = a
                department = ', '.join(affil_list[:i])
                location = ', '.join(affil_list[i+1::])
    dict_location = parse_location(location)
    dict_out = {'department': department,
                'institution': affil}
    dict_out.update(dict_location)
    return dict_out
