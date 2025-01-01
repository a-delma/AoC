import numpy as np
from functools import cache

import sys
sys.setrecursionlimit(5000)

file = 'temp.in'
# file = 'd17.in'
data = np.array([[int(c) for c in l] for l in open(file).read().splitlines()], dtype=np.int32)
data = np.pad(data, 1, 'constant', constant_values=9)

visited = {}

def minHeat(y, x, d, count):
    if y == data.shape[0] - 1 and x == data.shape[1] - 1:
        print(f'Reached Distination')
        return 0
    else:
        args = [(y - 1, x, 0, count + 1 if d == 0 else 0), 
                (y, x + 1, 1, count + 1 if d == 1 else 0), 
                (y + 1, x, 2, count + 1 if d == 2 else 0), 
                (y, x - 1, 3, count + 1 if d == 3 else 0)]
        possible = []
        for a in args:
            if a[2] >= 3:
                continue
            elif 1 < a[0] < data.shape[0] - 1:
                continue
            elif 1 < a[1] < data.shape[1] - 1:
                continue
            elif (a[0], a[1]) in visited:
                continue
            else:
                possible.append(minHeat(*a))
        if len(possible) == 0:
            best = 99999999999
        else:
            best = min(possible) + data[y, x]
        visited[(y,x)] = best
        return best
            
print(minHeat(1, 1, 0, 0))
