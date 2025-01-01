import numpy as np
from speed import *
import networkx as nx
import re

# data = open('input/temp').read().splitlines()
data = open('input/d18').read().splitlines()

coords = [[int(y) for y in re.findall(r'\d+', x )] for x in data]
b = (71, 71)
grid = np.zeros(b, dtype=int)

def getGraph(grid):
    rows, cols = grid.shape
    graph = nx.Graph()
    for r in range(rows):
        for c in range(cols):
            graph.add_node((r, c))
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if inBounds(nr, nc, grid):
                    graph.add_edge((r, c), (nr, nc))
    return graph

start = (0, 0)
end   = (70, 70)

seconds = 1024
G1 = getGraph(grid)
for x, y in coords[:seconds]:
    G1.remove_node((x, y))
print(nx.shortest_path_length(G1, start, end))

count = 0
G2 = getGraph(grid)
while True:
    x, y = coords[count]
    G2.remove_node((x, y))
    if count % 100 == 0:
        print(count)
    try:
        path = nx.shortest_path_length(G2, start, end)
    except nx.NetworkXNoPath:
        print(x, y)
        break
    count += 1
