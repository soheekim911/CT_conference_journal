import time
import csv
import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

edgelist = []
f1 = csv.reader(open('journal_author.csv','r'))
for row in f1:
    edgelist.append((row[0],row[1]))
# print(edgelist)

Journal = []
Name= []
for i in edgelist:
    # print(i[0] + ', ' + i[1])
    Journal.append(i[0])
    Name.append(i[1])


B = nx.Graph()
B.add_nodes_from(Name, bipartite=0)
B.add_nodes_from(Journal, bipartite=1)
B.add_edges_from(edgelist)

projected = nx.projected_graph(B, Name)
plt.figure(1,figsize=(10,10), dpi=300, facecolor = "blue",edgecolor="green") 
nx.draw(projected, with_labels=True)
