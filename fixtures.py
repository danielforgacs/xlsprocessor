xls = (
    (
        (None,              None,               None,               None),
        ('name',            None,               None,               None),
        (None,              'name',             None,               None),
        (None,              None,               'name',             None),
        ('name',            None,               'name',             None),
        ('name',            'code',             'area 1',           'area 2'), # OK
        ('area 1',          'area 2',           'area 3',           'area 4'), # OK
        ('area 1',          'area 2',           None,               'area 4'),
        ('name',            None,               'area 1',           'area 2'),
        ('name',            'code',             None,               'area 2'),
        ('name',            'code',             'khkjh',            'area 2'),
    ),
    (
        (None,              None,               None,               None),
        ('name',            None,               None,               None),
        (None,              'name',             None,               None),
        (None,              None,               'name',             None),
        ('name',            None,               'name',             None),
        ('name',            'code',             'area 1',           'area 2'), # OK
        ('area 1',          'area 2',           'area 3',           'area 4'), # OK
        ('area 1',          'area 2',           None,               'area 4'),
        ('name',            None,               'area 1',           'area 2'),
        ('name',            'code',             None,               'area 2'),
        ('name',            'code',             'khkjh',            'area 2'),
    ),
)

xls_cellclasses = (
    (
        ('NameLabelCell',   'CodeLabelCell',    'AreaCell',         'AreaCell'),
        ('AreaCell',        'AreaCell',         'AreaCell',         'AreaCell'),
    ),
    (
        ('NameLabelCell',   'CodeLabelCell',    'AreaCell',         'AreaCell'),
        ('AreaCell',        'AreaCell',         'AreaCell',         'AreaCell'),
    ),
)

xls_celltruth = (
    (
        (True,              True,               True,               True),
        (True,              True,               True,               True),
    ),
    (
        (True,              True,               True,               True),
        (True,              True,               True,               True),
    ),
)

xls_rowclasses = (
    (
        'NameAreaRow',
        'AreaRow'
    ),
    (
        'NameAreaRow',
        'AreaRow'
    ),
)

xls_ok_rowindexes = (
    (
        5,
        6,
    ),
    (
        5,
        6,
    ),
)
