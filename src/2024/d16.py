import numpy as np
from speed import *

data = open('input/temp').read().splitlines()
data = open('input/d16').read().splitlines()


data = np.array([[x for x in y] for y in data])
s = next(getCoords('S', data))
s += (1, )
e = next(getCoords('E', data))


def dijkstra(s):
    dims = data.shape + (4, )
    dist = np.ones(dims, dtype=int) * np.inf
    prev = np.full(dims, fill_value=np.nan, dtype=object)
    Q = [(idx, jdx, kdx) for idx, i in enumerate(data) for jdx, j in enumerate(i) for kdx in range(4) if j != '#']
    dist[s] = 0
    print(f"Looking from {s} in map with {len(Q)} nodes")
    while Q:
        if len(Q) % 100 == 0:
            print(len(Q))
        Q = sorted(Q, key=lambda x: dist[x], reverse=True)
        x, y, f = Q.pop()
        neighbors = [((x, y, (f + 1) % 4), 1000), ((x, y, (f - 1) % 4), 1000)]
        foward = (x + dirs[f][0], y + dirs[f][1], f)
        if foward in Q:
            neighbors.append((foward, 1))
        for p1, d in neighbors: 
            altDist = d + dist[x, y, f]
            if altDist < dist[p1]:
                prev[p1] = [(x, y, f)]
                dist[p1] = altDist
            elif altDist == dist[p1]:
                prev[p1].append((x, y, f))
    return dist, prev

dist, prev = dijkstra(s)
toFill = np.zeros_like(data)


def reverse(cur, s):
    if toFill[cur[:2]] == 1:
        return
    elif cur[:2] == s[:2]:
        toFill[cur[:2]] = 1
        return
    else:
        toFill[cur[:2]] = 1
    for n in prev[cur]:
        reverse(n, s)

print(minDist := min(dist[e]))
ends = np.where(dist[e] == minDist)[0]

for d in ends:
    reverse(e + (d, ), s)
    
# printArrayWithIndices(toFill)

print(np.sum(toFill == '1'))