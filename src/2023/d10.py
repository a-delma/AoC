import numpy as np
import networkx as nx

import matplotlib.pyplot as plt

file = 'temp.in'
file = 'd10.in'
data = open(file).read().splitlines()
x, y = len(data[0]), len(data)

# print(data, x, y)
G = nx.DiGraph()

for ydx, row in enumerate(data):
    for xdx, tile in enumerate(row):
        match tile:
            case '|':
                G.add_edge((ydx-1, xdx), (ydx, xdx))
                G.add_edge((ydx+1, xdx), (ydx, xdx))
                # G.add_edge((ydx, xdx), (ydx-1, xdx))
                # G.add_edge((ydx, xdx), (ydx+1, xdx))
            case '-':
                G.add_edge((ydx, xdx-1), (ydx, xdx))
                G.add_edge((ydx, xdx+1), (ydx, xdx))
                # G.add_edge((ydx, xdx),(ydx, xdx-1))
                # G.add_edge((ydx, xdx),(ydx, xdx+1))
            case 'L':
                G.add_edge((ydx-1, xdx), (ydx, xdx))
                G.add_edge((ydx, xdx+1), (ydx, xdx))
                # G.add_edge((ydx, xdx), (ydx-1, xdx))
                # G.add_edge((ydx, xdx), (ydx, xdx+1))
            case 'J':
                G.add_edge((ydx-1, xdx), (ydx, xdx))
                G.add_edge((ydx, xdx-1), (ydx, xdx))
                # G.add_edge((ydx, xdx), (ydx-1, xdx))
                # G.add_edge((ydx, xdx), (ydx, xdx-1))
            case '7':
                G.add_edge((ydx+1, xdx), (ydx, xdx))
                G.add_edge((ydx, xdx-1), (ydx, xdx))
                # G.add_edge((ydx, xdx), (ydx+1, xdx))
                # G.add_edge((ydx, xdx), (ydx, xdx-1))
            case 'F':
                G.add_edge((ydx+1, xdx), (ydx, xdx))
                G.add_edge((ydx, xdx+1), (ydx, xdx))
                # G.add_edge((ydx, xdx), (ydx+1, xdx))
                # G.add_edge((ydx, xdx), (ydx, xdx+1))
            case 'S':
                start = (ydx, xdx)

# print(list()

for (x, y) in filter(lambda x: x[0] == start, G.edges):
    G.add_edge(y, x)
paths = nx.single_source_shortest_path_length(G, start)
print(max(paths.values()))


# print(list(nx.simple_cycles(G)))

# nx.draw(G)
# plt.show()