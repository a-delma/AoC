import numpy as np
import networkx as nx

UP = [-1, 0]
RIGHT = [0, 1]
DOWN  = [1, 0]
LEFT  = [0, -1]

dirs = [UP, RIGHT, DOWN, LEFT]

def inBounds(x, y, arr = None):
    if arr is None:
        arr = y
        x, y = x
    arr = np.array(arr)
    return 0 <= x < arr.shape[0] and 0 <= y < arr.shape[1]

def printArrayWithIndices(array, width=2):
    # Get the shape of the array
    rows, cols = array.shape

    # Print the column indices
    colIndices = "      " + "  ".join(f"{i:>{width}}" for i in range(cols))
    print(colIndices)

    # Print the row indices and array content
    for i in range(rows):
        rowData = "  ".join(f"{array[i, j]:>{width}}" for j in range(cols))
        print(f"{i:>3} | {rowData}")

def getGraphWithExclusions(grid, excludeValue=1):
    graph = nx.Graph()
    for r, i in enumerate(grid):
        for c, j in enumerate(i):
            if j == excludeValue:
                continue  
            graph.add_node((r, c), value=j)
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if inBounds(nr, nc, grid) and grid[nr, nc] != excludeValue:
                    graph.add_edge((r, c), (nr, nc))
    return graph


def getCoords(s, arr):
    return (zip(*np.where(arr == s)))        

def flatten(xss):
    return [x for xs in xss for x in xs]