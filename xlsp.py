import xlrd
XLS_TEST = 'table.xls'
NAMELABEL = 'name'
CODELABEL = 'code'
NAMES = tuple(['name '+str(k) for k in range(5)])
AREAS = tuple(['area '+str(k) for k in range(5)])
COLOUR_DB = tuple(['colour '+str(k) for
                    k in range(5)])

class Cell(object):
    def __init__(self, value, idx):
        self.value = value
        self.idx = idx
    def __str__(self):
        objstr = super(Cell, self).__str__()
        return '<{0:<7}:{1:<5}: {2}>'.format(
            str(self.value), type(self).__name__,
            self.idx)
    def __nonzero__(self):
        return bool(self.value)

class Label(Cell):
    def __nonzero__(self):
        isgood = True
        if self.value == NAMELABEL:
            if self.idx != 0:
                isgood = False
        if self.value == CODELABEL:
            if self.idx != 1:
                isgood = False
        return isgood


class Name(Cell):
    pass

class Code(Cell):
    pass

class Area(Cell):
    pass

class Colour(Cell):
    pass


class XLS(object):
    def __init__(self, xlsfile):
        table = xlrd.open_workbook(
            filename=XLS_TEST)
        self.sheets = ()
        for sheet in table.sheets():
            initsheet = Sheet(sheet=sheet)
            if initsheet:
                self.sheets = self.sheets+(
                    initsheet,)
    def __iter__(self):
        return iter(self.sheets)
    def __nonzero__(self):
        return bool(self.sheets)

class Sheet(object):
    def __init__(self, sheet):
        self.name = sheet.name
        self.maxcoords = sheet.nrows, sheet.ncols
        self.rows = ()
        for rowidx in range(sheet.nrows):
            initrow = Row(
                row=sheet.row(rowidx), idx=rowidx)
            if initrow:
                self.rows = self.rows + (initrow,)
    def __str__(self):
        return '<{}:{}:rows {}: cols: {}>'.format(
            'sheet',
            self.name,
            self.maxcoords[0],
            self.maxcoords[1], )
    def __nonzero__(self):
        return bool(self.rows)

class Row(object):
    def __init__(self, row, idx):
        self.idx = idx
        self.cells = ()
        self.varbased = True
        for idx, rawcell in enumerate(row):
            cell = class_selector(
                cell=rawcell, cellidx=idx)
            if cell:
                self.cells = self.cells+(
                        cell,)
    def __str__(self):
        return '<{}:{}>'.format('Row', self.idx)
    def __nonzero__(self):
        return bool(self.cells)
    def __iter__(self):
        return iter(self.cells)

def class_selector(cell, cellidx):
    value = str(cell.value)
    if not value:
        return Cell(value=False, idx=cellidx)
    elif value == NAMELABEL:
        return Label(value=NAMELABEL, idx=cellidx)
    elif value == CODELABEL:
        return Label(value=CODELABEL, idx=cellidx)
    elif value in AREAS:
        return Area(value=value, idx=cellidx)
    else:
        return Colour(value=value, idx=cellidx)


if __name__ == '__main__':
    table = XLS(xlsfile=XLS_TEST)
    for sheet in table:
        print sheet
        for row in sheet.rows:
            print '\t', row, '\n\t\t',
            for cell in row:
                print cell,
            print
