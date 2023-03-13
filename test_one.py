def test_spaning_tree():
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


    # create a minimum spanning tree
    T = nx.minimum_spanning_tree(G)

    sum_path = []
    for i1 in range(len(edges)):
        for i2 in range(i1 + 1, len(edges)):
            for i3 in range(i2 + 1, len(edges)):
                for i4 in range(i3 + 1, len(edges)):
                    for i5 in range(i4 + 1, len(edges)):
                        sum_path.append(int(edges[i1][2] + edges[i2][2] + edges[i3][2] + edges[i4][2] + edges[i5][2]))
    # print(min(sum_path))
    # print(nx.tree.branching_weight(T))

    assert min(sum_path) == nx.tree.branching_weight(T)


