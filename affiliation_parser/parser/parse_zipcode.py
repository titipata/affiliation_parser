import re


def parse_zipcode(affil_text: str):
    """
    Parse zip code from given affiliation text

    https://github.com/unicode-org/cldr/blob/release-26-0-1/common/supplemental/postalCodeData.xml
    """
    zip_code_res = [
        r"\d{7}",
        r"\d{6}",
        r"\d{5}[-]?\d{4}?"
        r"\d{5}",
        r"\d{4}",
        r"\d{3}-\d{4}",
        r"\d{3}[ ]?\d{2}",
        r"\d{3}",
        r"\d{2}[ -]?\d{3}",
    ]

    zip_code = ""
    for code_re in zip_code_res:
        zip_code = re.search(code_re, affil_text)
        if zip_code:
            break

    zip_code_group = ""
    if zip_code:
        zip_code_group = zip_code.group()

    return zip_code_group
