# -*- coding: utf-8 -*-
import xlrd
import networkx as nx
import matplotlib.pyplot as plt


# 将二分网中的用户分为两类，（1. 只有出箭头的用户 2. 既有出箭头又有入箭头的用户）
# 分别对两类用户，绘制以上4个图：
# 1.	横坐标为产品的amount（代表金额），纵坐标为产品的度。
# 2.	横坐标为产品的Rate (代表利息)，纵坐标为产品的度。
# 3.	横坐标为产品的Term (代表周期)，纵坐标为产品的度。
# 4.	横坐标为产品的level (代表产品的风险等级)，纵坐标为产品的度。


if __name__ == '__main__':

    data_path = '../../../data/5W_new.xlsx'

    # 构建有向图
    G = nx.DiGraph()

    G1 = nx.Graph()
    G2 = nx.Graph()
    G3 = nx.Graph()
    G4 = nx.Graph()
    tenderer_nodes = []
    amount_nodes = []
    rate_nodes = []
    level_nodes = []
    term_nodes = []


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
            # 添加节点tenderer
            G.add_node(tenderer, {'color': 'blue'})
            # 添加节点product_id
            G.add_node(loaner, {'color': 'red'})
            # 添加边
            G.add_edge(tenderer, loaner)
            # G.add_weighted_edges_from([(tenderer, loaner, 1.0)])
    print("End to handle: ", sheetObj)
    print("****************************")

    # draw 二分无向图
    # pos = nx.shell_layout(G)
    # nx.draw_networkx(G, pos)
    # plt.show()

    both_users = []
    only_out_users = []

    print nx.info(G)
    in_degree_dict = G.in_degree_iter()
    out_degree_dict = G.out_degree_iter()
    for node in in_degree_dict:
        if node[1] == 0:
            only_out_users.append(node[0])
        else:
            both_users .append(node[0])

    # for key2 in out_degree_dict:
    #     print key2



