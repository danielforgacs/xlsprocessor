xls = (
(
    (None,              None,               None,               None),
    ('name',            None,               None,               None),
    (None,              'name',             None,               None),
    (None,              None,               'name',             None),
    ('name',            None,               'name',             None),
    ('name',            'code',             'area 1',           'area 2'),
    ('area 1',          'area 2',           'area 3',           'area 4'),
),
)

xls_cellclasses = (
(
    # ('EmptyCell',       'EmptyCell',        'EmptyCell',        'EmptyCell'),
    # ('NameLabelCell',   'EmptyCell',        'EmptyCell',        'EmptyCell'),
    # ('EmptyCell',       'NameLabelCell',    'EmptyCell',        'EmptyCell'),
    # ('EmptyCell',       'EmptyCell',        'NameLabelCell',    'EmptyCell'),
    # ('NameLabelCell',   'EmptyCell',        'NameLabelCell',    'EmptyCell'),
    ('NameLabelCell',   'CodeLabelCell',    'AreaCell',         'AreaCell'),
    ('AreaCell',        'AreaCell',         'AreaCell',         'AreaCell'),
),
)

xls_celltruth = (
(
    # (True,              True,               True,               True),
    # (True,              True,               True,               True),
    # (True,              False,              True,               True),
    # (True,              True,               False,              True),
    # (True,              True,               False,              True),
    (True,              True,               True,               True),
    (True,              True,               True,               True),
),
)

xls_ok_rowindexes = (
    (5, 6,),
)
