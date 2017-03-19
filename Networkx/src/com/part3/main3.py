# -*- coding: utf-8 -*-
import xlrd
import networkx as nx
import matplotlib.pyplot as plt


# 二）网络平均最短路径
#
# 1. 计算得到网络的平均最短路径L, 两节点之间的最短路径为：节点A到节点B所要经历的边的最小数目。网络的平均距离为所有节点对之间距离的平均值。得到一个数值。
# 2. 计算具有相同规模的随机网络的平均最短路径。得到一个数值。


if __name__ == '__main__':

    data_path = '../../../data/5W_new_test.xlsx'

    # 构建无向图
    G = nx.Graph()
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
            G.add_node(tenderer)
            # 添加节点product_id
            G.add_node(loan_id)
            # 添加边
            # G.add_edge(tenderer, loan_id)
            G.add_weighted_edges_from([(tenderer, loan_id, 1.0)])
    print("End to handle: ", sheetObj)
    print("****************************")

    # draw 二分无向加权图
    # pos = nx.shell_layout(G)
    # nx.draw_networkx(G, pos)
    # plt.show()

    print nx.info(G)
    g_nodes = G.number_of_nodes()
    g_edges = G.number_of_edges()
    g_sum_nodes = sum(G.degree().values())
    g_shortest_path = min(nx.all_pairs_shortest_path(G))
    g_clustering = nx.clustering(G)
    g_average_clustering = nx.average_clustering(G)
    print("G average_clustering ->", g_average_clustering)
    print("G clustering ->", g_clustering)
    print("G shortest path ->", g_shortest_path)

    G_tmp = nx.random_graphs.barabasi_albert_graph(g_nodes, g_edges)
    g_tmp_clustering = nx.clustering(G_tmp)
    g_tmp_average_clustering = nx.average_clustering(G_tmp)
    g_tmp_shortest_path = min(nx.all_pairs_shortest_path(G_tmp))
    print("G_tmp average_clustering ->", g_tmp_average_clustering)
    print("G_tmp clustering ->", g_tmp_clustering)
    print("G_tmp shortest path ->", g_shortest_path)

