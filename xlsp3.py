import fixtures
from pprint import pprint

NAMELABEL = 'name'
CODELABEL = 'code'
AREAS = ['area '+str(k) for k in range(5)]


class Table(object):
    def __init__(self, xls):
        self.sheets = tuple(Sheet(sheet) for sheet in xls)
    def __str__(self):
        return '\n'.join(['sheet:'+str(sheet) for sheet in self.sheets])

class Sheet(object):
    def __init__(self, sheet):
        cellrows = tuple(CellRow(row, idx) for idx, row in enumerate(sheet))
        self.rows = tuple(self.row_selector(cellrow=row) for row in cellrows)
    def row_selector(self, cellrow):
        return cellrow
    def __str__(self):
        return ''.join(['\n\trow: '+str(row.idx)+str(row) for row in self.rows])

class CellRow(object):
    def __init__(self, row, idx):
        self.idx = idx
        self.cells = tuple(self.cell_selector(cell, idx)
                        for idx, cell in enumerate(row))
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
    def __str__(self):
        return ', '.join([str(cell) for cell in self.cells])
        # cells = ', '.join([str(cell) for cell in self.cells])
        # return '<{}: {}>'.format(bool(self), cells)

class Row(object):
    pass

class EmptyRow(Row):
    pass

class AreaRow(Row):
    pass

class Cell(object):
    def __init__(self, value, idx):
        self.value = value
        self.idx = idx
    # def __str__(self):
    #     return '<{}. {}>'.format(self.value, bool(self))

class Empty(Cell):
    pass

class NameLabel(Cell):
    def __nonzero__(self):
        return self.idx == 0

class CodeLabel(Cell):
    def __nonzero__(self):
        return self.idx == 1

class AreaCell(Cell):
    pass


if __name__ == '__main__':
    table = Table(xls=fixtures.xls)
    print table
