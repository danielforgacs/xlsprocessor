import xlrd
XLS_TEST = 'table.xls'
NAMELABEL = 'name'
CODELABEL = 'code'
NAMES = tuple(['name '+str(k) for k in range(5)])
AREAS = tuple(['area '+str(k) for k in range(5)])
COLOUR_DB = tuple(['colour '+str(k) for
                    k in range(5)])

class Cell(object):
    def __init__(self, cellvalue, idx):
        self.value = cellvalue
        self.idx = idx
    def __str__(self):
        objstr = super(Cell, self).__str__()
        return '<"{0:<8}":{1:<10}: {2}>'.format(
            str(self.value), type(self).__name__,
            self.idx)
    def __nonzero__(self):
        return bool(self.value)

class NameLabel(Cell):
    def __nonzero__(self):
        return bool(self.idx==0)

class CodeLabel(Cell):
    pass

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
            newsheet = Sheet(sheet=sheet)
            if newsheet:
                self.sheets = self.sheets+(
                    newsheet,)
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
            newrow = Row(row=sheet.row(rowidx),
                idx=rowidx)
            if newrow:
                self.rows = self.rows + (newrow,)
    def __str__(self):
        return '<{}:{}:rows {}: cols: {}>'.format(
            'sheet', self.name, self.maxcoords[0],
            self.maxcoords[1], )
    def __nonzero__(self):
        return bool(self.rows)

class Row(object):
    def __init__(self, row, idx):
        self.idx = idx
        self.cells = ()
        for idx, rawcell in enumerate(row):
            newcell = class_selector(
                cellvalue=str(rawcell.value),
                cellidx=idx)
            self.cells = self.cells+(newcell,)
    def __str__(self):
        return '<{}:{}: {}>'.format('Row', self.idx,
            all(self.cells))
    def __nonzero__(self):
        # return all(self.cells)
        # return bool(self.cells)
        return True
    def __iter__(self):
        return iter(self.cells)

def class_selector(cellvalue, cellidx):
    if not cellvalue:
        return Cell(
            cellvalue=False,
            idx=cellidx,)
    elif cellvalue == NAMELABEL:
        return NameLabel(
            cellvalue=NAMELABEL,
            idx=cellidx,)
    elif cellvalue == CODELABEL:
        return CodeLabel(
            cellvalue=CODELABEL,
            idx=cellidx,)
    elif cellvalue in AREAS:
        return Area(
            cellvalue=cellvalue,
            idx=cellidx,)
    else:
        return Colour(
            cellvalue=cellvalue,
            idx=cellidx,)


if __name__ == '__main__':
    table = XLS(xlsfile=XLS_TEST)
    for sheet in table:
        print sheet
        for row in sheet.rows:
            print '\t', row, '\n\t\t',
            for cell in row:
                print cell,
            print
            print
