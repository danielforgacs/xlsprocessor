import xlsp3
import fixtures
import pytest


def test_01():
    table = xlsp3.Table(xls=fixtures.xls)
    for k, sheet in enumerate(table.sheets):
        for i, row in enumerate(sheet.rows):
            for j, cell in enumerate(row.cells):
                celltypename = fixtures.xls[k][i][j][1]
                is_cellvalid = fixtures.xls[k][i][j][2]
                assert type(cell).__name__ == celltypename
                assert bool(cell) == is_cellvalid


if __name__ == '__main__':
    pytest.main([
        __file__,
        '-s'
    ])
