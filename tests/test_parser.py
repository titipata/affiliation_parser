from affiliation_parser.parser import parse_email, parse_zipcode


def test_parse_email():

    assert parse_email("test@test") == ''
    assert parse_email("test@test.com") == 'test@test.com'


def test_parse_zip_code():
    assert parse_zipcode('123456') == '123456'