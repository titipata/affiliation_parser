# keyword list

DEPARMENT = frozenset(['laboratorio', 'laboratories', 'laboratory',
    'laboratoire', 'institute', 'academic', 'department'])

INSTITUTE = frozenset(['college', 'university', 'universitat',
    'unversiteit', 'universita', 'universidad', 'hospital',
    "ha'pital", 'istituti', 'istituto', 'institut', 'medical center', ' pharma',
    'riuniti', 'clinic', 'school of ', 'karolinska sjukhuset',
    'national institutes of health', 'cancer center', 'bioscience institute',
    'unilever research'])

COUNTRY = (
    ('italy', 'italia'),
    ('united kingdom', 'u.k.', '\buk\b', 'uk.', 'england', ' uk', 'liverpool'),
    ('united states of america', 'u.s.a', 'u. s. a.', 'united states', 'massachusetts', 'boston'),
    ('germany', 'frg', 'brd', 'f.r.g.', 'deutschland', 'engelskirchen', 'berlin',
     'hannover'),
    ('japan', 'keio University', 'jikei university', 'shiga university', 'jikei university',
     'niigata university', 'sendai city', 'shiba', 'asahikawa',
     'tokyo', 'yokohama', 'osaka', 'nagoya', 'sapporo', 'kobe', 'kyoto',
     'fukuoka', 'kawasaki', 'saitama', 'hiroshima', 'sendai', 'kitakyushu',
     'chiba', 'sakai', 'hamamatsu', 'niigata', 'shizuoka', 'okayama', 'asahikawa',
     'yamaguchi'),
    ('korea', 'seoul'),
    ('russia', 'moscow'),
    ('austria', 'linz'),
    ('israel', 'jerusalem', 'haifa'),
    ('norway', 'oslo'),
    ('finland', 'helsinki'),
    ('south africa', 'johannesburg'),
    ('france', 'paris', 'marseille'),
    ('canada', 'vancouver'),
    ('denmark', 'copenhagen'),
    ('china', 'china'),
    ('egypt', 'cairo'),
    ('poland', 'gdansk'),
    ('turkey', 'istanbul'),
    ('netherlands', 'utrecht'),
    ('belgium', 'belgium')
)

STATES = frozenset(['Alabama', 'Alaska', 'Arizona', 'Arkansas',
    'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida',
    'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa',
    'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland',
    'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri',
    'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey',
    'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio',
    'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina',
    'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia',
    'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'Washington DC',
    'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI',
    ' ID', ' IL', ' IN', ' IA', ' KS', ' KY', ' LA', ' ME', ' MD', ' MA', ' MI',
    'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC',
    'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT',
    'VT', 'VA', 'WA', 'WV', 'WI', 'WY', 'DC'])

UNIVERSITY_DUBLICATE = (
    ('university of california los angeles', 'ucla')
)
