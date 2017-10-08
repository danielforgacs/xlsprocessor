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
        return '<"{0:<8}":{1:<10}: {2} {3}>'.format(
            str(self.value), type(self).__name__,
            self.idx, bool(self))
    def __nonzero__(self):
        if self.idx == 0:
            return False
        else:
            return True

class NameLabel(Cell):
    def __nonzero__(self):
        return bool(self.idx==0)

class CodeLabel(Cell):
    def __nonzero__(self):
        return bool(self.idx==1)

class Name(Cell):
    pass

class Code(Cell):
    pass

class Area(Cell):
    def __nonzero__(self):
        return True

class Colour(Cell):
    def __nonzero__(self):
        return True


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
        self.is_namebased = False
        self.has_areas = False
        for rowidx in range(sheet.nrows):
            newrow = Row(row=sheet.row(rowidx),
                idx=rowidx)
            if newrow:
                # self.is_namebased = isinstance(newrow[0], NameLabel)
                # if self.is_namebased:
                #     if not isinstance(newrow[1], CodeLabel):
                #         break

                self.rows = self.rows + (newrow,)
    def __str__(self):
        return ('<{}:{}:rows {}: cols: {}: namebased: {}:'
            ' has areas: {}: valid: {}>').format(
            'sheet', self.name, self.maxcoords[0],
            self.maxcoords[1], self.is_namebased,
            str(self.has_areas), all(self.rows))
    def __nonzero__(self):
        # if not self.has_areas:
        #     return False
        return all(self.rows)

class Row(object):
    def __init__(self, row, idx):
        self.idx = idx
        self.cells = ()
        for idx, rawcell in enumerate(row):
            newcell = cell_selector(
                cellvalue=str(rawcell.value),
                cellidx=idx)
            self.cells = self.cells+(newcell,)
    def __str__(self):
        return '<{}:{}: {}>'.format(
            'Row', self.idx+1, all(self.cells))
    def __nonzero__(self):
        return all(self.cells)
    def __iter__(self):
        return iter(self.cells)
    def __getitem__(self, idx):
        return self.cells[idx]
    def __len__(self):
        return len(self.cells)

def cell_selector(cellvalue, cellidx):
    if not cellvalue:
        cellclass = Cell
        value = None
    elif cellvalue == NAMELABEL:
        cellclass = NameLabel
        value = NAMELABEL
    elif cellvalue == CODELABEL:
        cellclass = CodeLabel
        value = CODELABEL
    elif cellvalue in AREAS:
        cellclass = Area
        value = cellvalue
    else:
        cellclass = Colour
        value = cellvalue

    cell = cellclass(
            cellvalue=value,
            idx=cellidx,)

    return cell


if __name__ == '__main__':
    table = XLS(xlsfile=XLS_TEST)
    for sheet in table:
        pass
        print sheet
        for row in sheet.rows:
            pass
            print '\t', row, '\n\t\t',
            for cell in row:
                pass
                print cell,
            print
