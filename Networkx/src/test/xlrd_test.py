# -*- coding: utf-8 -*-
import xlrd
import matplotlib
matplotlib.use('TkAgg')
def read_excel(fileName):
    # 打开文件
    workbook = xlrd.open_workbook(fileName)

    # 获取所有sheet
    sheet_list = workbook.sheet_names()
    print sheet_list
    for sheet in sheet_list:
        print sheet


    # 根据sheet索引或者名称获取sheet内容
    # sheet索引从0开始
    sheet1 = workbook.sheet_by_index(0)
    # 根据名称获取Sheet
    sheet1 = workbook.sheet_by_name('Sheet1')

    # sheet的名称，行数，列数
    sheet_name = sheet1.name
    sheet_nrow = sheet1.nrows
    sheet_ncol = sheet1.ncols
    print sheet_name,sheet_nrow,sheet_ncol

    # 获取整行和整列的值（数组）
    # rows = sheet2.row_values(3) # 获取第四行内容
    # cols = sheet2.col_values(2) # 获取第三列内容
    # print rows
    # print cols

    # 获取单元格内容
    # print sheet2.cell(1,0).value.encode('utf-8')
    # print sheet2.cell_value(1,0).encode('utf-8')
    # print sheet2.row(1)[0].value.encode('utf-8')

    # 获取单元格内容的数据类型
    # print sheet2.cell(1,0).ctype

if __name__ == '__main__':
    read_excel('../../data/5W.xlsx')

