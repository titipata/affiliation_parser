# from ..data import UNIVERSITY_MULTIPLE_CAMPUS


def append_institution_city(affil: str, location: str):
    """
    Append city to university that has multiple campuses if exist
    """
    for university_list in UNIVERSITY_MULTIPLE_CAMPUS:
        if university_list[0] in affil.lower():
            for city in university_list[1::]:
                if city in location.lower() and not city in affil.lower():
                    affil = affil + " " + city
                    return affil
    return affil
