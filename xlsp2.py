import xlrd

NAMELABEL = 'name'
CODELABEL = 'code'
AREAS = ['area '+str(idx) for idx in range(10)]
COLOURS = ['colour '+str(idx) for idx in range(10)]

xls = 'table.xls'

table = xlrd.open_workbook(xls)

class Cell(object):
    def __init__(self, value, idx):
        self.value = value
        self.idx = idx
        # print '\t\t', self
    def __str__(self):
        return ('<{val:<8}.{idx:>2} .'
            '{boo:<6}.{typ}>').format(
            val=self.value,
            idx=self.idx+1,
            boo=str(bool(self)),
            typ=type(self).__name__)

class Empty(Cell):
    def __nonzero__(self):
        if self.idx == 0:
            return False
        else:
            return True

class Label(Cell):
    def __nonzero__(self):
        if self.idx == 0:
            return self.value == NAMELABEL
        elif self.idx == 1:
            return self.value == CODELABEL
        else:
            return False

class Area(Cell):
    pass



class Row(object):
    def __init__(self, cells, idx):
        self.cells =cells
        self.idx = idx
    def __str__(self):
        return ('Row: {idx}. type: {typ} valid:'
            ' {vld},\n\t{cels}\n').format(
            idx=self.idx+1,
            typ=self.__class__.__name__,
            vld=bool(self),
            cels='\n\t'.join([str(cell) for
                cell in self.cells]))

class AreaRow(Row):
    pass

class ColourRow(Row):
    pass




def walk(table):
    for sheet in table.sheets():
        # print 'sheet:', sheet.name
        for rowidx in range(sheet.nrows):
            # print '\trow idx:', rowidx+1
            rawrow = sheet.row(rowidx)
            rowcells = ()
            for cellidx, rawcell in enumerate(rawrow):
                # print '\t\tcell idx:', cellidx
                cell = tokenizer(
                    value=str(rawcell.value),
                    idx=cellidx)
                rowcells = rowcells + (cell,)
                # print '\t\t cell:', cell
            newrow = row_processor(
                cells=rowcells, idx=rowidx)
            print newrow


def tokenizer(value, idx):
    if not value:
        token = Empty
    elif value == NAMELABEL:
        token = Label
        value = NAMELABEL
    elif value == CODELABEL:
        token = Label
        value = CODELABEL
    elif value in AREAS:
        token = Area
        value = value
    return token(value=value, idx=idx)


def row_processor(cells, idx):
    if isinstance(cells[0], Label):
        return AreaRow(cells=cells, idx=idx)


table = walk(table=table)
# print table
