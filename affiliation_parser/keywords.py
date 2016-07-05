# keyword list

DEPARMENT = frozenset(['laboratorio', 'laboratories', 'laboratory',
    'institute', 'academic', 'department'])

INSTITUTE = frozenset(['college', 'university', 'universitat',
    'unversiteit', 'universita', 'universidad', 'hospital',
    "ha'pital", 'istituti', 'medical center', ' pharma',
    'riuniti', 'clinic'])

COUNTRY_DUBLICATE = (
    ('italy', 'italia'),
    ('u.k.', '\buk\b', 'uk.', 'united kingdom', 'england'),
    ('u.s.a', 'u. s. a.', 'united states', 'united states of america')
)

UNIVERSITY_DUBLICATE = frozenset(
    ('ucla', 'university of california los angeles')
)

COUNTRY_DUBLICATE = [
     {'keywords': ['keio University', 'jikei university', 'shiga university', 'tokyo', 'osaka'],
      'state': '',
      'country': 'Japan'},
     {'keywords': ['boston'],
     'states': 'Massachusetts',
     'country': 'United States'},
     {'keywords': ['f.r.g.'],
     'state': '',
     'country': 'Germany'}
]
