import networkx as nx
import numpy as np
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def inBounds(grid : np.array, x, y):
    return 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]

def gridToGraph(grid, toExclude = '#'):
    G = nx.Graph()
    for idx, i in enumerate(grid):
        for jdx, j in enumerate(i):
            if j == toExclude:
                continue
            G.add_node((idx, jdx))
            for dx, dy in dirs:
                if inBounds(grid, idx + dx, jdx + dy) and grid[idx + dx][jdx + dy] != toExclude:
                    G.add_edge(j, grid[idx + dx][jdx + dy])
    return G