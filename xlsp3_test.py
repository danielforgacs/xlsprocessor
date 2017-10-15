import xlsp3
import fixtures
import pytest


def test_01():
    table = xlsp3.Table(xls=fixtures.xls)
    for k, sheet in enumerate(table.sheets):
        for i, row in enumerate(sheet.rows):
            is_rowvalid = fixtures.xls_rowclasses[i]
            assert bool(row) == is_rowvalid
            for j, cell in enumerate(row.cells):
                celltypename = fixtures.xls_cellclasses[k][i][j]
                is_cellvalid = fixtures.xls_celltruth[k][i][j]
                assert type(cell).__name__ == celltypename
                assert bool(cell) == is_cellvalid


if __name__ == '__main__':
    pytest.main([
        __file__,
        '-s'
    ])
