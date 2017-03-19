# -*- coding: utf-8 -*-
import xlrd
import networkx as nx
import matplotlib.pyplot as plt


# 一. 度和度分布
# 1.	对网络中所有节点的度求平均，得到网络的平均度，即把所有节点的度相加再除以节点数， 得到一个数值。
# 2.	画出网络度分布图：横坐标为度K，纵坐标为节点的度为K的概率。
#       为网络中度为的节点在整个网络中所占的比率，也就是，在网络中随机抽取到度为的节点的概率为，
#       即，x:度，y:度的概率

if __name__ == '__main__':

    data_path = '../../../data/5W_new.xlsx'

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
            G.add_node(tenderer, {'color': 'blue'})
            # 添加节点product_id
            G.add_node(loan_id, {'color': 'red'})
            # 添加边
            # G.add_edge(tenderer, loan_id)
            G.add_weighted_edges_from([(tenderer, loan_id, 1.0)])
    print("End to handle: ", sheetObj)
    print("****************************")

    # draw 二分无向图
    # pos = nx.shell_layout(G)
    # nx.draw_networkx(G, pos)
    # plt.show()

    print nx.info(G)
    g_nodes = G.number_of_nodes()
    g_sum_nodes = sum(G.degree().values())
    # g_shortest_path = nx.diameter(G)
    # g_average_shortest_path = nx.average_shortest_path_length(G)
    g_clustering = nx.clustering(G)
    g_average_degree = (float(g_sum_nodes)/float(g_nodes))
    g_average_clustering = nx.average_clustering(G)
    print("G average_clustering ->", g_average_clustering)
    print("G clustering ->", g_clustering)
    print("G average_degree->", g_average_degree)

    degree = nx.degree_histogram(G)
    x = range(len(degree))
    y = [z/float(sum(degree)) for z in degree]
    plt.loglog(x, y)
    plt.show()

