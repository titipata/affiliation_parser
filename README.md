# Affiliation Parser

(work in progress)

Simple parser for MEDLINE and Pubmed Open-Access affiliation string.
We can parse multiple fields from the affiliation string including department, affiliation, location, country, email and zip code from affiliation text.


## Example

```python
from affiliation_parser import parse_affil
parse_affil("Department of Health Science, Kochi Women's University, Kochi 780-8515, Japan. watanabe@cc.kochi-wu.ac.jp")
```

output is a dictionary

```python
{'country': 'japan',
 'department': 'Department of Health Science',
 'email': 'watanabe@cc.kochi-wu.ac.jp',
 'full_text': "Department of Health Science, Kochi Women's University, Kochi , Japan. ",
 'institution': "Kochi Women's University",
 'location': 'Kochi , Japan',
 'zipcode': '780-8515'}
```
