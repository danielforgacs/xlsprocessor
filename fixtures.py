xls = (
(
    (None,              None,               None,               None),
    ('name',            None,               None,               None),
    (None,              'name',             None,               None),
    (None,              None,               'name',             None),
    ('name',            None,               'name',             None),
),
)

xls_cellclasses = (
(
    ('EmptyCell',       'EmptyCell',        'EmptyCell',        'EmptyCell'),
    ('NameLabelCell',   'EmptyCell',        'EmptyCell',        'EmptyCell'),
    ('EmptyCell',       'NameLabelCell',    'EmptyCell',        'EmptyCell'),
    ('EmptyCell',       'EmptyCell',        'NameLabelCell',    'EmptyCell'),
    ('NameLabelCell',   'EmptyCell',        'NameLabelCell',    'EmptyCell'),
),
)

xls_celltruth = (
(
    (True,              True,               True,               True),
    (True,              True,               True,               True),
    (True,              False,              True,               True),
    (True,              True,               False,              True),
    (True,              True,               False,              True),
),
)
