import re


def parse_email(affil_text: str):
    """Find email from given string"""
    match = re.search(r"[\w\.-]+@[\w\.-]+", affil_text)
    if match is not None:
        email = match.group()
        if email[-1] == ".":
            email = email[:-1]
    else:
        email = ""
    return email
