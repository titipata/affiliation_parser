# Affiliation Parser

(work in progress)

Simple parser for MEDLINE and Pubmed Open-Access affiliation string.
We aim to parse multiple fields from the string including department,
affiliation, city and country from affiliation text.


## Example

```python
from affiliation_parser import parse_affil
parse_affil('Diabetes Research Unit, University of Wales College of Medicine, Cardiff, U.K.')
```
