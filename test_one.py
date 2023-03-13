def test_spaning_tree():
    import networkx as nx
    from matplotlib import pyplot as plt
    import random

    class DisjointSets:
        def __init__(self, n):
            self.n = n
            self.parent = [None] * (self.n + 1)
            self.size = [1] * (self.n + 1)

        def findRoot(self, node):
            return node if self.parent[node] == None else self.findRoot(self.parent[node]) 

        def ask(self, a, b):
            root_a = self.findRoot(a)
            root_b = self.findRoot(b)

            return root_a == root_b

        def join(self, a, b):
            root_a = self.findRoot(a)
            root_b = self.findRoot(b)
            
            if root_a == root_b:
                pass
            else:
                if self.size[root_a] >= self.size[root_b]:
                    self.parent[root_b] = root_a
                    self.size[root_a] += self.size[root_b]
                else:
                    self.parent[root_a] = root_b
                    self.size[root_b] += self.size[root_a]
    def kruskal(graph):
        edges = sorted(graph, key=lambda edge: edge[2])
        mst = []
        ds = DisjointSets(len(graph))
        total_cost = 0
        for (a, b, w) in edges:
            if not ds.ask(a, b):
                mst.append((a, b, w))
                total_cost += w
                ds.join(a, b)
        return total_cost

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


    # create a minimum spanning tree
    T = nx.minimum_spanning_tree(G)

    # print(nx.tree.branching_weight(T))

    assert kruskal(edges) == nx.tree.branching_weight(T)


