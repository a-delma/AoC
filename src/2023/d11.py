import numpy as np
from itertools import combinations, accumulate

starMap = np.array([[c for c in l] for l in open('d11.in').read().splitlines()])
galaxies = list(accumulate([[[ydx, xdx] for xdx, x in enumerate(y) if x == '#'] for ydx, y in enumerate(starMap)]))[-1]

def incrementRows(array, galaxies, amt=1):
    galaxies = np.array(galaxies)
    for arr, i in [(array, 0), (array.T, 1)]:
        for idx, r in enumerate(reversed(arr)):
            if np.all(r == '.'):
                galaxies[galaxies[:, i] > (arr.shape[i] - idx - 1), i] += amt
    return galaxies
print([np.array([(abs(x2 - x1) + abs(y2 - y1)) for (x1, y1), (x2, y2) in combinations(incrementRows(starMap, galaxies.copy(), i-1), 2)], dtype=np.uint64).sum() for i in [2, 1000000]])

