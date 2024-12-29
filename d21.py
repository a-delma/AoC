import numpy as np
from functools import cache
import networkx as nx
from speed2 import *

A = -2
data = open("input/temp").read().splitlines()
# data = open("input/2024/d21").read().splitlines()

numPad = np.array([[7, 8, 9], [4, 5, 6], [1, 2, 3], [-1, 0, A]])
numGraph = gridToGraph(numPad, -1)

arrowPad = np.array([[-1, 0, A], [3, 2, 1]])
arrowGrid = gridToGraph(arrowPad, -1)

@cache
def enterNumberFrom(s, e, numPad = 1):
    G = numGraph if numPad else arrowGrid
    path = nx.shortest_path(G, s, e)
    print(path)
    exit()
    return '1'

cur = A
pat = ''
for i in data:
    for j in list(i):
        pat += enterNumberFrom(cur, j) + str(A)
        cur = i

print(pat)

@cache
def getArrowPresses(s):
    pass
