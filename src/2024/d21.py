import numpy as np
from functools import cache
from src.speed import *
from itertools import *

A = -2
data = open("input/temp").read().splitlines()
data = open("input/2024/d21").read().splitlines()

def makeDict(grid):
    return {j : np.array([idx, jdx]) for idx, i in enumerate(grid) for jdx, j in enumerate(i)}
numPad = np.array([[7, 8, 9], [4, 5, 6], [1, 2, 3], [-1, 0, A]])
arrowPad = np.array([[' ', '^', 'A'], ['<', 'v', '>']])

numGraph = makeDict(numPad)
arrowGraph = makeDict(arrowPad)

def findPaths(d):
    y, x = d
    horiz = '>' if x < 0 else '<'
    vert = 'v' if y < 0 else '^'
    paths = permutations([horiz for _ in range(abs(x))] + [vert for _ in range((abs(y)))], int(np.sum(np.abs(d))))
    return set(paths)

def checkPath(s, p, num = 1, invalid = -1):
    G = numGraph if num else arrowGraph
    pad = numPad if num else arrowPad
    i, j = G[s]
    for d in p:
        if d == '>':
            j += 1
        elif d == '<':
            j -= 1
        elif d == 'v':
            i += 1
        elif d == '^':
            i -= 1
        if pad[(i, j)] == invalid:
            return False
    return True

def checkChanges(p):
    total = 0
    for i in range(len(p) - 1):
        if p[i] != p[i + 1]:
            total += 1
    return total

@cache
def enterNumberFrom(s, e, numPad = 1):
    G = numGraph if numPad else arrowGraph
    d = G[s] - G[e]
    paths = ["".join(p) for p in findPaths(d) if checkPath(s, p, numPad, -1 if numPad else ' ')]
    paths = sorted(paths, key = scorePath if numPad else checkChanges, reverse=False)
    return paths[0]

def scoreChar(c):
    match c:
        case '>':
            return 1
        case '<':
            return 3
        case 'v':
            return 2
        case '^':
            return 1
def scorePath(p):
    return scoreChar(p[-1]) + checkChanges(p) * 20


numRobots = 25
scores = []
for i in data:
    target = ''
    cur = A
    for j in i:
        j = A if j == 'A' else int(j)
        target += enterNumberFrom(cur, j) + 'A'
        cur = j
    
    for r in range(numRobots):
        print(r, len(target))
        cur = 'A'
        curRobo = ''
        for j in target:
            curRobo += enterNumberFrom(cur, j, 0) + 'A'
            cur = j
        target = curRobo
            
    scores.append((len(curRobo) , int(i[:-1])))

print(scores)
print(sum([l * n for (l, n) in scores]))

