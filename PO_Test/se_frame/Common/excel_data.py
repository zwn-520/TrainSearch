# encoding=utf-8
import xlrd, os
import sys
from datetime import datetime
from xlrd import xldate_as_tuple

sys.path.append(r'D:\PythonSeleniumTest\PO_Test\se_frame\Common')
from function import project_path


def read_excel(filename, index):
    xls = xlrd.open_workbook(filename)
    sheet = xls.sheet_by_index(index)

    dic = {}
    for i in range(sheet.nrows):
        data = []
        for j in range(sheet.ncols):
            ctype = sheet.cell(i, j).ctype  # 表格的数据类型
            cell = sheet.cell_value(i, j)
            if ctype == 2 and cell % 1 == 0:  # 如果是整形
                cell = int(cell)
            elif ctype == 3:
                # 转成datetime对象
                date = datetime(*xldate_as_tuple(cell, 0))
                cell = date.strftime('%Y-%m-%d')
            elif ctype == 4:
                cell = True if cell == 1 else False
            data.append(cell)
        dic[i] = data
    return dic


if __name__ == '__main__':
    data = read_excel(project_path() + "Data\\testdata.xlsx", 0)
    print(data)
    print(data.get(1))
