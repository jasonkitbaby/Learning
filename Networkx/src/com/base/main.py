# -*- coding: utf-8 -*-
import xlrd
import networkx as nx
import numpy as np
import matplotlib
# matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite


#
#
#  两个单顶点网络进行统计计算
#  平均度、最短路径长度和聚类系数统计值

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
    tenderer_nodes = []
    loan_id_nodes = []
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
            tenderer_nodes.append(tenderer)
            # 添加节点product_id
            G.add_node(loan_id)
            loan_id_nodes.append(loan_id)
            # 添加边
            # G.add_edge(tenderer, loan_id)
            G.add_weighted_edges_from([(tenderer, loan_id, 1.0)])
            print("End to handle: ", sheetObj)
    print("****************************")
    print nx.info(G)

    # draw 二分无向图
    pos = nx.shell_layout(G)
    nx.draw_networkx(G, pos)
    # plt.show()

    # 投影
    NSet = bipartite.sets(G)
    user = nx.project(G, set(tenderer_nodes))  # 向user节点投影
    product = nx.project(G, set(loan_id_nodes))  # 向product节点投影

    # 单顶点用户
    G1 = bipartite.projected_graph(G, user)
    nx.draw_networkx(G1, pos)
    plt.show()
    print nx.info(G1)
    g1_nodes = G1.number_of_nodes()
    g1_sum_nodes = sum(G1.degree().values())
    # g1_shortest_path = nx.diameter(G1)
    # g1_average_shortest_path = nx.average_shortest_path_length(G1)
    g1_shortest_path = min(nx.all_pairs_shortest_path(G1))
    g1_clustering = nx.clustering(G1)
    g1_average_degree = (float(g1_sum_nodes)/float(g1_nodes))
    g1_average_clustering = nx.average_clustering(G1)
    print("G1 average_clustering ->", g1_average_clustering)
    print("G1 clustering ->", g1_clustering)
    print("G1 average_degree->", g1_average_degree)
    print("G1 shortest path->", g1_shortest_path)

    # 单顶点产品
    G2 = bipartite.projected_graph(G, product)
    nx.draw_networkx(G1, pos)
    plt.show()
    print nx.info(G2)
    g2_nodes = G2.number_of_nodes()
    g2_sum_nodes = sum(G2.degree().values())
    g2_clustering = nx.clustering(G2)
    g2_average_degree = (float(g2_sum_nodes)/float(g2_nodes))
    g2_average_clustering = nx.average_clustering(G2)
    g2_shortest_path = min(nx.all_pairs_shortest_path(G1))
    print("G2 clustering ->", g2_clustering)
    print("G2 average_clustering ->", g2_average_clustering)
    print("G2 average_degree->", g2_average_degree)
    print("G2 shortest path->", g2_shortest_path)