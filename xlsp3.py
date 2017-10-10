import fixtures
from pprint import pprint

NAMELABEL = 'name'
CODELABEL = 'code'
AREAS = ['area '+str(k) for k in range(5)]
COLOURS = ['colour '+str(k) for k in range(5)]


class Table(object):
    def __init__(self, xls):
        self.sheets = tuple(Sheet(sheet) for sheet in xls)

class Sheet(object):
    def __init__(self, sheet):
        self.rows = tuple(Row(row) for row in sheet)
        print self
    def __str__(self):
        return '\n'.join([str(row) for row in self.rows])

class Row(object):
    def __init__(self, row):
        self.cells = tuple(self.cell_selector(cell, idx)
                        for idx, cell in enumerate(row))
    def __str__(self):
        cells = ', '.join([str(cell) for cell in self.cells])
        return '<{}: {}>'.format(bool(self), cells)
    def cell_selector(self, value, idx):
        if not value:
            cellclass = Empty
        elif value == NAMELABEL:
            cellclass = NameLabel
        elif value == CODELABEL:
            cellclass = CodeLabel
        elif value in AREAS:
            cellclass = AreaCell
        return cellclass(value=value, idx=idx)

class Cell(object):
    def __init__(self, value, idx):
        self.value = value
        self.idx = idx
    def __str__(self):
        return '<{}. {}>'.format(
            self.value, bool(self))

class Empty(Cell):
    pass

class NameLabel(Cell):
    def __nonzero__(self):
        return self.idx == 0

class CodeLabel(Cell):
    pass

class AreaCell(Cell):
    pass




if __name__ == '__main__':
    table = Table(xls=fixtures.xls)

