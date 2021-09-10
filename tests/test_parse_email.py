from affiliation_parser.parser import parse_email


def test_parse_email():

    assert parse_email("test@test") == ''
    assert parse_email("test@test.com") == 'test@test.com'
