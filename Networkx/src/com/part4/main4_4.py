# -*- coding: utf-8 -*-
import xlrd
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite


# 在构建“用户----产品”二分网基础上，绘制4个图：
# 4.	横坐标为产品的level (代表产品的风险等级)，纵坐标为产品的度。


if __name__ == '__main__':

    data_path = '../../../data/5W_new_test.xlsx'

    # 构建无向图
    G4 = nx.Graph()
    tenderer_nodes = []
    level_nodes = []
    print("**************************")
    print("    Begin computing   ")
    print("    Open file from -> " + data_path)
    # 打开文件
    workbook = xlrd.open_workbook(data_path)
    sheet_list = workbook.sheet_names()
    print("    Sheets : ")
    print sheet_list
    for sheetObj in sheet_list:
        print("   Load Data from  " + sheetObj)
        sheet = workbook.sheet_by_name(sheetObj)
        # sheet的名称，行数，列数
        sheet_name = sheet.name
        sheet_nrow = sheet.nrows
        sheet_ncol = sheet.ncols
        print("    Sheet Name :", sheet_name)
        print("    Sheet Row Count : ", sheet_nrow)
        print("    Sheet Col Count : ", sheet_ncol)
        # Column A ,0 产品 loanid
        # Column B ,1 借款人
        # Column C ,2 借款金额
        # Column D ,3 借款利息
        # Column E ,4 借款周期
        # Column F ,5 投标人用户
        # Column G ,6 进度
        # Column H ,7 风险等级字幕
        # Column I ,8 风险等级数字
        for row_index in range(1, sheet_nrow-1):
            # print("record Id  ", row_index)
            loan_id = sheet.cell(row_index, 0).value
            loaner = sheet.cell(row_index, 1).value
            amount = int(sheet.cell(row_index, 2).value)
            rate = sheet.cell(row_index, 3).value
            term = sheet.cell(row_index, 4).value
            tenderer = sheet.cell(row_index, 5).value
            level = sheet.cell(row_index, 8).value

            tenderer_nodes.append(tenderer)
            level_nodes.append(level)

            # 产品的level
            G4.add_node(tenderer, {'color': 'blue'})
            G4.add_node(level, {'color': 'red'})
            G4.add_weighted_edges_from([(tenderer, level, 1.0)])


    print("****************************")

    print ('build g4')
    print nx.info(G4)
    # G4_NSet = bipartite.sets(G4)
    # G4_user = nx.project(G4, G4_NSet[0])
    G4_level = nx.project(G4, level_nodes)
    G4_level_degree_dict = nx.degree(G4_level)
    y4 = []
    x4 = []
    for key in G4_level_degree_dict.keys():
        x4.append(key)
        y4.append(G4_level_degree_dict[key])
    print(x4)
    print(y4)
    print(G4_level_degree_dict)
    plt.plot(x4, y4)
    plt.show()

