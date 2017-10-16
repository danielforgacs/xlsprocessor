import xlsp
import fixtures
import pytest


def test_cells():
    table = xlsp.Table(xls=fixtures.xls)
    for k, sheet in enumerate(table.sheets):
        for i, row in enumerate(sheet.rows):
            for j, cell in enumerate(row.cells):
                celltypename = fixtures.xls_cellclasses[k][i][j]
                is_cellvalid = fixtures.xls_celltruth[k][i][j]
                assert type(cell).__name__ == celltypename
                assert bool(cell) == is_cellvalid

def test_rows():
    table = xlsp.Table(xls=fixtures.xls)
    for k, sheet in enumerate(table.sheets):
        for i, row in enumerate(sheet.rows):
            assert row.idx == fixtures.xls_ok_rowindexes[k][i]


if __name__ == '__main__':
    pytest.main([
        __file__,
        '-s'
    ])
