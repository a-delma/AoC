import numpy as np
from speed import *

data = open('input/temp').read().splitlines()
# data = open('input/d20').read().splitlines()

data = np.array([list(x) for x in data])

grid = getGraphWithExclusions(data)
start = next(getCoords('S', data))
end = next(getCoords('E', data))

defaultPath = nx.shortest_path_length(grid, start, end)
