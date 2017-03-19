# -*- coding: utf-8 -*-
import xlrd
import networkx as nx
import numpy
import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt


def read_excel():
    a = 5000
    b = 3000
    c = max(a, b)
    d = range(c)
    x = d
    y = range(5000)

    plt.plot(x, y)
    plt.show()

if __name__ == '__main__':
    read_excel()