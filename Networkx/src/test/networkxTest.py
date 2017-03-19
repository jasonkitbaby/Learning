# -*- coding: utf-8 -*-
import xlrd
import networkx as nx
import numpy as np
import matplotlib
# matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite

if __name__ == '__main__':

    print "hello world"

    B = nx.Graph()

    B.add_edge('a', 201)
    B.add_edge('a', 202)
    B.add_edge('a', 203)

    B.add_edge('b', 203)
    B.add_edge('b', 204)

    B.add_edge('c', 204)
    B.add_edge('c', 205)

    B.add_edge('d', 201)
    B.add_edge('d', 203)
    B.add_edge('d', 205)

    B.add_edge('e', 201)
    B.add_edge('e', 202)
    B.add_edge('e', 203)
    B.add_edge('e', 204)
    B.add_edge('e', 205)


    # pos = nx.random_layout(B)  # positions for all nodes
    # nx.draw_networkx(B, pos, node_size=70, font_size=0)
    # plt.show()

    NSet = bipartite.sets(B)
    Act = nx.project(B, NSet[0])  # 向项目节点投影
    Actor = nx.project(B, NSet[1])  # 向参与者节点投影

    G1 = bipartite.projected_graph(B, Act)
    G2 = bipartite.projected_graph(B, Actor)


    # circular_layout(G[, dim, scale, center])
    # fruchterman_reingold_layout(G[, dim, k, ...])
    # random_layout(G[, dim, scale, center])
    # shell_layout(G[, nlist, dim, scale, center])
    # spring_layout(G[, dim, k, pos, fixed, ...])
    # spectral_layout(G[, dim, weight, scale, center

    pos = nx.shell_layout(G1)  # positions for all nodes
    nx.draw_networkx(G1, pos, node_size=500, font_size=-1)
    plt.show()

    pos = nx.shell_layout(G2)  # positions for all nodes
    nx.draw_networkx(G2, pos, node_size=500, font_size=-1)
    plt.show()

    # print Act.edges()
