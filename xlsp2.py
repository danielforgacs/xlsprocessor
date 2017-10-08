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
        print self
    def __str__(self):
        return '<{val}:{idx}:{boo}:{typ}>'.format(
            val=self.value,
            idx=self.idx+1,
            boo=bool(self),
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

def walk(table):
    for sheet in table.sheets():
        # print sheet.name
        for rowidx in range(sheet.nrows):
            rawrow = sheet.row(rowidx)
            newrow = ()
            # print 'row index:', rowidx+1
            for cellidx, rawcell in enumerate(rawrow):
                cell = tokenizer(
                    value=rawcell.value,
                    idx=cellidx)
                newrow = newrow + (cell,)


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





table = walk(table=table)
# print table
