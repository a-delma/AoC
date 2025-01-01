import numpy as np
from Lib.heapq import *

file = 'temp.in'
# file = 'd17.in'
data = np.array([[int(c) for c in l] for l in open(file).read().splitlines()], dtype=np.int32)
# data = np.pad(data, 1, 'constant', constant_values=9)


curNode = (0, 0)
visited = {(0, 0) : 0}
toVisit = [(0, 1), (1, 0)]
toVisit = [(data[*c], c, (0, -1)) for c in toVisit]
heapify(toVisit)

while toVisit:
    h, (y, x), (d, c1) = heappop(toVisit)    
    if (y, x) not in visited:
        visited[(y,x)] = h
        for d1, c in enumerate([(y-1, x), (y, x+1), (y+1, x), (y, x-1)]):
            newCount = c1 + 1 if d == d1 else 0
            if c not in visited and newCount < 3:
                if c[0] not in [-1, data.shape[0]] and c[1] not in [-1, data.shape[1]]:
                    heappush(toVisit, (h + data[*c], c, (d1, newCount)))
print(visited[(data.shape[0] - 1, data.shape[1] - 1)])

# for ydx, y in enumerate(data):
#     for xdx, x in enumerate(y):
#         print(f'{visited[(ydx, xdx)]:03d} ', end='')
#     print()
            
