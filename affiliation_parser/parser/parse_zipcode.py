def parse_zipcode(affil_text: str):
    """
    Parse zip code from given affiliation text
    """
    zip_code_group = ""
    zip_code = re.search(r"(\d{5})([-])?(\d{4})?", affil_text)
    if zip_code is None:
        zip_code = re.search(r"(\d{3})([-])?(\d{4})?", affil_text)
    else:
        zip_code = ""
    if zip_code:
        zip_code_group = zip_code.groups()
        zip_code_group = [p for p in zip_code_group if p is not None]
        zip_code_group = "".join(zip_code_group)
    return zip_code_group
