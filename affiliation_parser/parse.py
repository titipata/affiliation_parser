from .keywords import *

def parse_affil(affil_text):
    """
    Parse affiliation string to institution and department
    """
    affil_list = affil_text.split(', ')
    affil = ''
    department = ''
    for i, a in enumerate(affil_list):
        for ins in INSTITUTE:
            if ins in a.lower():
                affil = a
                department = ' '.join(affil_list[:i])
    dict_out = {'institution': affil,
                'department': department}
    return dict_out
