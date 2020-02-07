import xlrd, xlwt

# with xlrd.open_workbook('test.xlsx') as rf:  # 卡开excel文件，一个excel文件包含多个表
#     sheet = rf.sheet_by_name('Sheet1')  # 读取excel表,这里有多重方式rf.sheets() rf.sheet_by_name() rf.sheet_by_index()，得到一个对象
#     # rows = sheet.nrows  # 获取表格行数
#     # cols = sheet.ncols  # 获取表格列数
#     # cell = sheet.cell(0, 0)  # 读取一个格的内容，参数的坐标
#     # cell_type = cell.ctype  # 内容的类型，枚举类型，详见xlrd.XL_CELL_TEXT 为1 xlrd.XL_CELL_NUMBER 为2……
#     # cell_value = cell.value  # 内容
#     # #row和col所有方法的使用类型
#     # cell_row = sheet.row(0)  # 读取一行内容，参数是行号，返回列表
#     # cell_row_values = sheet.row_values(1, 2, 3)  # 参数1行号，2从第二列开始，3第三列结束,1必填，2,3选填
#     # print(sheet.row_slice(1,2,3))#切片操作，参数1行号，2从第二列开始，3第三列结束,1必填，2,3选填
#     # print(sheet.row_len(1))# 行长度
#     # print(cell_row_values)
#     # cell_col = sheet.col(0)  # 读取一列内容，参数是列号，返回列表
#     # print(sheet.col_types(1, 2, 3))  # 参数1行号，2从第二列开始，3第三列结束,1必填，2,3选填
#     nc = sheet.ncols
#     result = sheet.put_cell(0, nc, xlrd.XL_CELL_TEXT, u'总分', None)  # 写入内容
with xlrd.open_workbook('test.xlsx') as rbook:
    rsheet = rbook.sheet_by_name('Sheet1')
    nc = rsheet.ncols
    rsheet.put_cell(0, nc, xlrd.XL_CELL_TEXT, u'总分', None)
    for row in range(1, rsheet.nrows):
        t = sum(rsheet.row_values(row, 1))
        rsheet.put_cell(row, nc, xlrd.XL_CELL_NUMBER, t, None)
wbook = xlwt.Workbook()
wsheet = wbook.add_sheet(rsheet.name)
style = xlwt.easyxf('align: vertical center')
for r in range(rsheet.nrows):
    for c in range(rsheet.ncols):
        wsheet.write(r, c, rsheet.cell_value(r, c), style)
wbook.save('test_new.xls')
