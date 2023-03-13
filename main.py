import networkx as nx
from matplotlib import pyplot as plt
import random

G = nx.Graph()

n = 6
# create nodes to the graph
G.add_nodes_from([int(i) for i in range(1, n + 1)])

# add edges to the graph
edges = []
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        w = random.randint(1, 10)
        edges.append((i, j, w))

G.add_weighted_edges_from(edges)


# draw graph with edge labels
vertex_pos=nx.spring_layout(G)

vertex_pos[1] = [0, 0]
vertex_pos[2] = [1, 5]
vertex_pos[3] = [1, 10]
vertex_pos[4] = [-1, 5]
vertex_pos[5] = [-1, 10]
vertex_pos[6] = [0, 15]

nx.draw(G, with_labels=True, pos = vertex_pos)
nx.draw_networkx_edge_labels(G, pos=vertex_pos, edge_labels=nx.get_edge_attributes(G,'weight'))

plt.savefig("Graph.png")

# create a minimum spanning tree
T = nx.minimum_spanning_tree(G)

# draw the minimum spanning tree in red
nx.draw(T, with_labels=True, pos=vertex_pos)
nx.draw_networkx_edges(T, pos=vertex_pos, edge_color='r')
nx.draw_networkx_edge_labels(T, pos=vertex_pos, edge_labels=nx.get_edge_attributes(T,'weight'))

plt.savefig("graph-with-mst-2.png")
plt.show()