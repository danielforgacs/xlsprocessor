xls = (
    (# sheet1
        (None,      None,       None,       None),# empty       # false
        ('name',    None,       None,       None),# namearea    # true
        (None,      'name',     None,       None),# bad         # false
        (None,      None,       'name',     None),# bad         # false
        ('name',    None,       'name',     None),# bad         # false

    ),(# sheet1
        (None,      None,       None,       None), # empty      # false
        ('code',    None,       None,       None), # bad        # false
        (None,      'code',     None,       None), # bad        # false
        (None,      None,       'code',     None), # bad        # false
        ('code',    None,       'code',     None), # bad        # false
    ),

    (# sheet2
        ('name',    'code',     'area 1',   'area 2'), # NameArea
        ('name',    'code',     'area 1',   'area 2'), # NameArea
        ('name',    'code',     'area 1',   'area 2'), # NameArea
    )
)

