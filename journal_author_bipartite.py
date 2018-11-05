import time
import csv
import networkx as nx
from networkx.algorithms import bipartite

# startTime = datetime.datetime.now()

# rename files
infile = 'journal_author.csv'
# name_outfile = infile.replace('.csv', 'bipartite.csv.')
# print 'Files renamed at: ' + str(datetime.datetime.now() - startTime)

# load CSV into a dict
with open(infile, 'r') as csv_file:
    rawData = list(csv.DictReader(csv_file))
# print 'Files loaded at: ' + str(datetime.datetime.now() - startTime)

# create edgelist for Name -x- Event relationships
edgelist = []
for i in rawData:
	edgelist.append(
    (i['Journal'],
     i['Name'])    
    )
# print 'Bipartite edgelist created at: ' + str(datetime.datetime.now() - startTime)

# deduplicate edgelist
edgelist = sorted(set(edgelist))
# print 'Bipartite edgelist deduplicated at: ' + str(datetime.datetime.now() - startTime)

# create a unique list of Name and Event for nodes
Journal = sorted(set([i['Journal'] for i in rawData]))
Name = sorted(set([i['Name'] for i in rawData]))
# print 'Node entities deduplicated at: ' + str(datetime.datetime.now() - startTime)

# add nodes and edges to a graph
B = nx.Graph()
B.add_nodes_from(Journal, bipartite=0)
B.add_nodes_from(Name, bipartite=1)
B.add_edges_from(edgelist)
# print 'Bipartite graph created at: ' + str(datetime.datetime.now() - startTime)

# create bipartite projection graph
name_nodes, journal_nodes = bipartite.sets(B)
pos = {}

pos.update((node, (1, index)) for index, node in enumerate(name_nodes))
pos.update((node, (2, index)) for index, node in enumerate(journal_nodes))

journal_nodes = set(n for n,d in B.nodes(data=True) if d['bipartite']==0)
name_nodes = set(B) - journal_nodes
name_graph = bipartite.weighted_projected_graph(B, name_nodes)
# print 'Single-mode projected graph created at: ' + str(datetime.datetime.now() - startTime)

# write graph to CSV
# nx.write_weighted_edgelist(name_graph, name_outfile, delimiter=',')
# print 'Single-mode weighted edgelist to CSV: ' + str(datetime.datetime.now() -    startTime)

nx.draw(B,with_labels=True)

# endTime = datetime.datetime.now()
