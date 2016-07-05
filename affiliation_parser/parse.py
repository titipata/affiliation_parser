import re
from unidecode import unidecode
from .keywords import *

def find_country(location):
    """
    Find country from string
    """
    location_lower = location.lower()
    for country in COUNTRY:
        for c in country:
            if c in location_lower:
                return country[0]
    return ''

def check_usa(affil_text):
    for state in STATES:
        if state in location:
            return 'united states of america'
    return ''

def parse_location(location):
    """
    Parse location to zipcode and location
    """
    zip_code_group = ''
    zip_code = re.search('(\d{5})([-])?(\d{4})?', location)
    if zip_code is not None:
        zip_code_group = zip_code.groups()
        zip_code_group = [p for p in zip_code_group if p is not None]
        zip_code_group = ''.join(zip_code_group)
    location = re.sub(zip_code_group, '', location)
    location = re.sub('\.', '', location).strip()
    country = find_country(location)
    dict_location = {'location': location,
                     'country': country,
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
    departments = list()
    if department == '':
        for i, a in enumerate(affil_list):
            for dep in DEPARMENT:
                if dep in a.lower():
                    departments.append(affil_list[i])
        department = ', '.join(departments)
    dict_location = parse_location(location)
    dict_out = {'full_text': affil_text,
                'department': department,
                'institution': affil}
    dict_out.update(dict_location)
    if dict_out['country'] == '':
        dict_out['country'] = check_usa(affil_text)
    return dict_out
