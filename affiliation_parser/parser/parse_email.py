import re


def parse_email(affil_text: str):
    """Find email from given string
    
    email format RFC is extremely complicated:
    https://www.ietf.org/rfc/rfc5322.txt
    
    
    a simple re from http://emailregex.com/
    """
    match = re.search(r"([a-zA-Z0-9.+_-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)",
                      affil_text)
    if match is not None:
        email = match.group()
        if email[-1] == ".":
            email = email[:-1]
    else:
        email = ""
    return email
