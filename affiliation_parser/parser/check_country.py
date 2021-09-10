def check_country(affil_text: str):
    """
    Check if any states string from USA or UK
    """
    for country in ["UK"]:
        if country in affil_text:
            return "united kingdom"
    for state in STATES:
        if state in affil_text:
            return "united states of america"
    return ""
