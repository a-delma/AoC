import numpy as np
from itertools import combinations
from speed import *

data = open('input/temp').read().splitlines()
data = open('input/d8').read().splitlines()

data = np.array([[x for x in y] for y in data])
nodeLocations = zip(*np.where(data != '.'))

nodes = {}
for (x, y) in nodeLocations:
    sym = data[x, y]
    n = nodes.get(sym, [])
    n.append((x, y))
    nodes[sym] = n 

def findAnti(p1, p2):
    dist = np.array(p2) - np.array(p1)
    n1 = p2 + dist
    dist = np.array(p1) - np.array(p2)
    n2 = p1 + dist
    return n1, n2

antiNodes = set()
for _, v in nodes.items():
    for (p1, p2) in combinations(v, 2):
        # print(p1, p2)
        n1, n2 = findAnti(p1, p2)
        for i, j in [n1, n2]:
            if inBounds(i, j, data):
                antiNodes.add((int(i), int(j)))
        
print(len(antiNodes))

def findMultiNodes(p1, p2):
    nodes = set()
    for i, j in [(p1, p2), (p2, p1)]:
        dist = np.array(i) - np.array(j)
        k = 0
        while inBounds(x := (k * dist + j), data):
            nodes.add((tuple(x)))
            k += 1
        # print(i, j)
        # print(nodes)
        # exit()
    # print(nodes)
    return nodes


multiNodes = set()
for _, v in nodes.items():
    for (p1, p2) in combinations(v, 2):
        multiNodes = multiNodes | findMultiNodes(p1, p2)
        
print(len(multiNodes))
