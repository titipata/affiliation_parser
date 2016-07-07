import re
from unidecode import unidecode
from .keywords import *

def clean_text(affil_text):
    """
    Given affiliation text with abbreviation, clean that text
    """
    affil_text = re.sub('Dept. ', 'Department ', affil_text)
    affil_text = re.sub('Surg. ', 'Sugery ', affil_text)
    affil_text = re.sub('Univ. ', 'University ', affil_text)
    return affil_text

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
    """
    Check if any states string from USA. If so, it will return country string
    """
    for state in STATES:
        if state in affil_text:
            return 'united states of america'
    return ''

def parse_email(affil_text):
    """Find email from given string"""
    match = re.search(r'[\w\.-]+@[\w\.-]+', affil_text)
    if match is not None:
        email = match.group()
        if email[-1] == '.':
            email = email[:-1]
    else:
        email = ''
    return email

def parse_zipcode(affil_text):
    """
    Parse zip code from given affiliation text
    """
    zip_code_group = ''
    zip_code = re.search('(\d{5})([-])?(\d{4})?', affil_text)
    if zip_code is None:
        zip_code = re.search('(\d{3})([-])?(\d{4})?', affil_text)
    if zip_code is not None:
        zip_code_group = zip_code.groups()
        zip_code_group = [p for p in zip_code_group if p is not None]
        zip_code_group = ''.join(zip_code_group)
    return zip_code_group

def parse_location(location):
    """
    Parse location and country from affiliation string
    """
    location = re.sub('\.', '', location).strip()
    country = find_country(location)
    dict_location = {'location': location,
                     'country': country}
    return dict_location

def parse_affil(affil_text):
    """
    Parse affiliation string to institution and department
    """
    affil_text = unidecode(affil_text)
    affil_text = clean_text(affil_text)
    email = parse_email(affil_text)
    zip_code = parse_zipcode(affil_text)
    affil_text = re.sub(email, '', affil_text)
    affil_text = re.sub(zip_code, '', affil_text)

    affil_list = affil_text.split(', ')
    affil = list()
    department = ''
    location = list()
    for i, a in enumerate(affil_list):
        for ins in INSTITUTE:
            if ins in a.lower():
                if not a in affil:
                    affil.append(a)
                location = affil_list[i+1::]

    # remove unwanted from list
    for i, a in enumerate(affil):
        for rm in REMOVE_INSTITUE:
            if rm in a.lower() and (not 'university' in a.lower()):
                affil.pop(i)
    for i, l in enumerate(location):
        for rm in DEPARMENT:
            if rm in l.lower():
                location.pop(i)
    affil = ', '.join(affil)
    location = ', '.join(location)
    if location == '':
        location = affil_text.split(', ')[-1]

    if department == '':
        departments = list()
        for i, a in enumerate(affil_list):
            for dep in DEPARMENT:
                if dep in a.lower():
                    departments.append(affil_list[i])
        department = ', '.join(departments)
    dict_location = parse_location(location)
    dict_out = {'full_text': affil_text,
                'department': department,
                'institution': affil,
                'email': email,
                'zipcode': zip_code}
    dict_out.update(dict_location)
    if dict_out['country'] == '':
        dict_out['country'] = check_usa(affil_text)
    return dict_out
