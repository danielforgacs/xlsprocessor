xls = (
    (# sheet1
        (None, None, None, None), # empty
        ('name', None, None, None), # name area
        (None, 'name', None, None), # bad
        (None, None, 'name', None), #  bad
        ('name', None, 'name', None), # bad
    ),(# sheet1
        (None, None, None, None), # empty
        ('code', None, None, None), # bad
        (None, 'code', None, None), # bad
        (None, None, 'code', None), # bad
        ('code', None, 'code', None), # bad
    ),
    (# sheet2
        ('name', 'code', 'area 1', 'area 2'), # NameArea
        ('name', 'code', 'area 1', 'area 2'), # NameArea
        ('name', 'code', 'area 1', 'area 2'), # NameArea
    )
)

