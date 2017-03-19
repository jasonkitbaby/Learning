

[TOC]

# Excel fun #
TODO define A level
=IF(I220="AA",1,IF(I220="B",2,IF(I220="C",3,IF(I220="D",4,IF(I220="E",5,IF(I220="F",6))))))

TBD: conver days
=if(ISERROR(EFIND("天",E3)),E3,LEFT(E3,FIND("天",E3)-1))


# network x #
## Graph Type ##
| Graph Type | NetworkX Class |
|-----------------------------|
| Undirected Simple  | Graph |
| Directed Simple | DiGraph |
| With Self-loops | Graph, DiGraph |
| With Parallel edges | MultiGraph, MultiDiGraph |

## Direct  Graph ##
The DiGraph class provides additional methods specific to directed edges, 
e.g. DiGraph.out_edges(), DiGraph.in_degree(), DiGraph.predecessors(), DiGraph.successors() etc.
To allow algorithms to work with both classes easily, the directed versions of neighbors() and degree() are equivalent to successors() and the sum of in_degree() and out_degree() respectively even though that may feel inconsistent at times.
reference : https://networkx.readthedocs.io/en/stable/reference/classes.digraph.html

## 网络图模型 ##
http://www.cnblogs.com/forstudy/archive/2012/03/20/2407954.html
https://networkx.readthedocs.io/en/stable/reference/generators.html

fast_gnp_random_graph(n, p[, seed, directed]) 	Returns a G_{n,p} random graph, also known as an Erdős-Rényi graph or a binomial graph.
gnp_random_graph(n, p[, seed, directed]) 	Returns a G_{n,p} random graph, also known as an Erdős-Rényi graph or a binomial graph.
dense_gnm_random_graph(n, m[, seed]) 	Returns a G_{n,m} random graph.
gnm_random_graph(n, m[, seed, directed]) 	Returns a G_{n,m} random graph.
erdos_renyi_graph(n, p[, seed, directed]) 	Returns a G_{n,p} random graph, also known as an Erdős-Rényi graph or a binomial graph.
binomial_graph(n, p[, seed, directed]) 	Returns a G_{n,p} random graph, also known as an Erdős-Rényi graph or a binomial graph.
newman_watts_strogatz_graph(n, k, p[, seed]) 	Return a Newman–Watts–Strogatz small-world graph.
watts_strogatz_graph(n, k, p[, seed]) 	Return a Watts–Strogatz small-world graph.
connected_watts_strogatz_graph(n, k, p[, ...]) 	Returns a connected Watts–Strogatz small-world graph.
random_regular_graph(d, n[, seed]) 	Returns a random d-regular graph on n nodes.
barabasi_albert_graph(n, m[, seed]) 	Returns a random graph according to the Barabási–Albert preferential attachment model.
powerlaw_cluster_graph(n, m, p[, seed]) 	Holme and Kim algorithm for growing graphs with powerlaw degree distribution and approximate average clustering.
duplication_divergence_graph(n, p[, seed]) 	Returns an undirected graph using the duplication-divergence model.
random_lobster(n, p1, p2[, seed]) 	Returns a random lobster graph.
random_shell_graph(constructor[, seed]) 	Returns a random shell graph for the constructor given.
random_powerlaw_tree(n[, gamma, seed, tries]) 	Returns a tree with a power law degree distribution.
random_powerlaw_tree_sequence(n[, gamma, ...]) 	Returns a degree sequence for a tree with a power law distribution.

## quick start ##
http://blog.sina.com.cn/s/blog_bcf91a2f0102voqz.html
http://blog.sina.com.cn/s/blog_720448d301018px7.html
http://blog.sciencenet.cn/home.php?mod=space&uid=404069&do=blog&classid=141080&view=me&from=space


# Numpy #
## one ##

# Matplotlib #
Draw networkx with matplotlib

reference : https://networkx.readthedocs.io/en/stable/reference/drawing.html

install matplotlib
http://matplotlib.org/users/installing.html

## matplotlib back List ##
reference  https://my.oschina.net/swuly302/blog/94915
```
import matplotlib
matplotlib.use('PS') # 默认生成postscript输出。
如果你使用use命令，必须在import matplotlib.pyplot或者matplotlib.pylab之前设置。
```

## Matplotlib 渲染器 ##
| 渲染器 | 文件类型 | 描述 |
|-----------------------| 
| AGG | png | 光栅图 –使用 Anti-Grain Geometry 高质量渲染引擎 |
| PS  | ps eps| 矢量图 – Postscript 输出 |
| PDF | pdf | 矢量图– 可携带格式 |
| SVG | svg | 矢量图 – 可伸缩矢量图形 |
| Cairo | png ps pdf svg |矢量图 – Cairo图 |
| GDK | png jpg tiff | 光栅图 – gimp |

## Position Layout ##
| layout | comment |
| ----------------| 
| circular_layout(G[, dim, scale, center]) 	| Position nodes on a circle. |
| fruchterman_reingold_layout(G[, dim, k, ...]) 	| Position nodes using Fruchterman-Reingold force-directed algorithm. |
| random_layout(G[, dim, scale, center]) 	| Position nodes uniformly at random. 
| shell_layout(G[, nlist, dim, scale, center]) 	| Position nodes in concentric circles. |
| spring_layout(G[, dim, k, pos, fixed, ...]) 	| Position nodes using Fruchterman-Reingold force-directed algorithm. |
| spectral_layout(G[, dim, weight, scale, center]) 	| Position nodes using the eigenvectors of the graph Laplacian. |




# 图的指标 #
1. 图的平均度: 即把所有节点的度相加再除以节点数， 得到一个数值。
2。图的最短路径：
3. 群聚系数统计值：
    平均群聚系统
4. 度的概率：


```
Name:代表用户名 
Loan_Id: 代表理财产品编号 
每个理财产品包括4个属性： 
1.amount代表金额 
2. Rate代表利息 
3. Term代表周期 
4.level代表这个理财产品的风险等级
```

# Python 安装 #

# 使用Pip 安装 python 库 #
reference: http://www.ttlsa.com/python/how-to-install-and-use-pip-ttlsa/
```
pip install numpy
pip install matplotlib
pip install networkx

```





## python之matplotlib中plt.show()不显示图的解决办法 ##
http://www.jianshu.com/p/3f4b89aaf057
https://www.python.org/download/mac/tcltk/

| 渲染器 | 文件类型 | 描述 |
|-----------------------| 
| AGG | png | 光栅图 –使用 Anti-Grain Geometry 高质量渲染引擎 |
| PS  | ps eps| 矢量图 – Postscript 输出 |
| PDF | pdf | 矢量图– 可携带格式 |
| SVG | svg | 矢量图 – 可伸缩矢量图形 |
| Cairo | png ps pdf svg |矢量图 – Cairo图 |
| GDK | png jpg tiff | 光栅图 – gimp |




# uninstall activeTCL #
http://stackoverflow.com/questions/21843328/uninstall-active-tcl-mac






# 作业 #
## base ##

1。无向加权网络图
2。投影
    A.	单顶点用户网络的平均度、最短路径长度和聚类系数统计值。
    B.	单顶点产品网络的平均度、最短路径长度和聚类系数统计值。
    

## 一. 度和度分布 ##

1.	对网络中所有节点的度求平均，得到网络的平均度，即把所有节点的度相加再除以节点数， 得到一个数值。
2.	画出网络度分布图：横坐标为度K，纵坐标为节点的度为K的概率。
    为网络中度为的节点在整个网络中所占的比率，也就是，在网络中随机抽取到度为的节点的概率为，
    即，x:度，y:度的概率

## 二. 群聚系数 ##
1. 计算得到网络的平均集聚系数C, 计算的是网络中与同一个节点连接的两节点之间也相互连接的平均概率。得到一个数值。
2. 计算具有相同规模的随机网络的平均聚集系数。。得到一个数值。
3. 在求得各节点集聚系数的基础上，可以得到度为的节点的集聚系数的平均值，绘制下方统计图
4. 进一步再把上图画在双对数坐标下



# 要画的图 #
1.	横坐标为产品的amount（代表金额），纵坐标为产品的度。
2.	横坐标为产品的Rate (代表利息)，纵坐标为产品的度。
3.	横坐标为产品的Term (代表周期)，纵坐标为产品的度。
4.	横坐标为产品的level (代表产品的风险等级)，纵坐标为产品的度。



集聚系数与聚度------x:度,,  Y: 当前度所有节点的平均 nx.average_clustering(G)
最短路径长度--------
        nx.diameter(G)返回图G的直径（最长最短路径的长度），
        nx.average_shortest_path_length(G)则返回图G所有节点间平均最短路径长度
        degree =  nx.degree_histogram(G)          #返回图中所有节点的度分布序列​
        G = nx.random_graphs.barabasi_albert_graph(1000,3)   #生成一个n=1000，m=3的BA无标度网络

3. 用户兴趣分析
x:纬度（amount,rate)，y:当前值的度的平均


4. 区分用户
   只有出度， both