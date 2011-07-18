#!/usr/bin/env python
#ex: set ts=4 et:

# find the shortest route from my cubicle to coffee

import networkx as nx

# Graph creation
G = nx.Graph()

# path cost
G.add_edge('cubicle','hallway-printer', weight=20)
G.add_edge('hallway-printer','kitchen-local', weight=30)
G.add_edge('kitchen-local','coffee', weight=3)
G.add_edge('hallway-printer','inter-building-crossroads', weight=16)
G.add_edge('inter-building-crossroads','kitchen-other', weight=4)
G.add_edge('kitchen-other','coffee', weight=4)
G.add_edge('inter-building-crossroads','robo-door', weight=10)
G.add_edge('robo-door','elevators', weight=5)
G.add_edge('robo-door','bathroom', weight=20)

if __name__ == '__main__':

    import random
    import matplotlib.pyplot as plt

    print('graph has %d nodes with %d edges' % (
          nx.number_of_nodes(G), nx.number_of_edges(G)))
    print(nx.number_connected_components(G), 'connected components')

    try:
        from networkx import graphviz_layout
    except ImportError:
        raise ImportError("This example needs Graphviz and either PyGraphviz or Pydot")

    plt.figure(1, figsize=(8,8))
    # layout graphs with positions using graphviz neato
    pos = nx.graphviz_layout(G)
    pos=nx.spring_layout(G)
    # color nodes the same in each connected subgraph
    C = nx.connected_component_subgraphs(G)
    #for G in C:
    #c = [random.random()]*nx.number_of_nodes(G) # random color...
    nx.draw(G, pos,
             font_size=16,
             node_size=50000,
             node_color=[0] * nx.number_of_nodes(G),
             with_labels=False)
    plt.savefig('coffee-path.png', dpi=75)

