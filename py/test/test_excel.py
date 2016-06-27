import xlrd

fileName = r'E:\git\pythonCode\src\test.xls'

bk = xlrd.open_workbook(fileName)
try:
    sh = bk.sheet_by_name("参赛者信息")
    # 获取行数
    nrows = sh.nrows
    # 获取列数
    ncols = sh.ncols
    print("nrows %d, ncols %d" % (nrows, ncols))

    # 获取各行数据
    
    for i in range(1, nrows):
        row_data = sh.row_values(i)
        cell_value = sh.cell_value(i, 1)
        xlrd.xldate_as_tuple(cell_value, 0)
        # print(xlrd.xldate_as_tuple(cell_value, 0))
        # print(cell_value)
        print(row_data)

except Exception as e:
    print("no sheet in %s named 参赛者信息" % fileName)

