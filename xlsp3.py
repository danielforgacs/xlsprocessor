# cell classes:
# - empty
# - name label
# - code label
# - name
# - code
# - area
# - colour
#
# row classes:
# - empty
# - named area
# - named colour
# - area
# - colour


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
        if all([isinstance(cell, EmptyCell) for cell in cellrow]):
            rowclass = EmptyRow
        elif not all(cellrow):
            rowclass = EmptyRow
        elif isinstance(cellrow[0], NameLabelCell):
            rowclass = NameAreaRow
        elif isinstance(cellrow[0], AreaCell):
            rowclass = NameAreaRow
        else:
            return cellrow
        return rowclass(cellrow.cells, cellrow.idx)
    def __str__(self):
        return ''.join(['\n\t{:<2} {:<6} {:<11} {}'.format(
            str(row.idx), str(bool(row)), str(type(row).__name__),
            str(row)) for row in self.rows])
        return ''.join(['\n\trow: '+str(row.idx)+' '+str(bool(row))+' '+str(type(row).__name__)
            +' '+str(row) for row in self.rows])

class CellRow(object):
    def __init__(self, row, idx):
        self.idx = idx
        self.cells = tuple(self.cell_selector(cell, idx)
                        for idx, cell in enumerate(row))
    def cell_selector(self, value, idx):
        if not value:
            cellclass = EmptyCell
        elif value == NAMELABEL:
            cellclass = NameLabelCell
        elif value == CODELABEL:
            cellclass = CodeLabelCell
        elif value in AREAS:
            cellclass = AreaCell
        return cellclass(value=value, idx=idx)
    def __str__(self):
        return ', '.join([str(cell) for cell in self.cells])
    def __iter__(self):
        return iter(self.cells)
    def __getitem__(self, idx):
        return self.cells[idx]

class Row(object):
    def __init__(self, cells, idx):
        self.cells = cells
        self.idx = idx
    def __str__(self):
        return ', '.join([str(cell) for cell in self.cells])

class EmptyRow(Row):
    def __nonzero__(self):
        return False

class AreaRow(Row):
    def __nonzero__(self):
        is_areacell = lambda x: isinstance(x, AreaCell)
        return all(map(is_areacell, self.cells))

class NameAreaRow(Row):
    def __nonzero__(self):
        if not all(self.cells):
            return False

        cellclasses = ('NameLabelCell', 'CodeLabelCell',)
        cellclasses = cellclasses + tuple(['AreaCell' for k in self.cells[2:]])
        matches = []
        for cell, cellclass in zip(self.cells, cellclasses):
            matches.append(type(cell).__name__ == cellclass)
        return all(matches)


class Cell(object):
    def __init__(self, value, idx):
        self.value = value
        self.idx = idx
    def __str__(self):
        return '<{:<7} {:<2} {:<10}>'.format(
            self.value, '.' if bool(self) else 'x',
            self.__class__.__name__)

class EmptyCell(Cell):
    pass

class NameLabelCell(Cell):
    def __nonzero__(self):
        return self.idx == 0

class CodeLabelCell(Cell):
    def __nonzero__(self):
        return self.idx == 1

class AreaCell(Cell):
    pass


if __name__ == '__main__':
    table = Table(xls=fixtures.xls)
    print table
