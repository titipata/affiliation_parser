import re


def parse_email(affil_text: str):
    """Find email from given string
    
    email format RFC is extremely complicated:
    https://www.ietf.org/rfc/rfc5322.txt
    
    
    a simple re from http://emailregex.com/
    """

    texts = affil_text.split(' ')[-1]

    match = re.search(r"([a-zA-Z0-9.+_-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)",
                      texts[-1])
    if match is not None:
        email = match.group()
        email.rstrip('.')

    else:
        email = ""

    return email
