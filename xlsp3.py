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

class Row(object):
    def __init__(self, row):
        # self.cells = tuple(Cell(cell) for cell in row)
        self.cells = tuple(self.cell_selector(cell)
                            for cell in row)
        print self
    def __str__(self):
        return ', '.join([str(cell) for cell in self.cells])
    def cell_selector(self, value):
        if not value:
            cellclass = Empty
        elif value == NAMELABEL:
            cellclass = NameLabel
        elif value == CODELABEL:
            cellclass = CodeLabel
        elif value in AREAS:
            cellclass = AreaCell
        return cellclass(value=value)

class Cell(object):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)

class Empty(Cell):
    pass

class NameLabel(Cell):
    pass

class CodeLabel(Cell):
    pass

class AreaCell(Cell):
    pass




if __name__ == '__main__':
    table = Table(xls=fixtures.xls)

