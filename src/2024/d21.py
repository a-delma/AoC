import numpy as np
from functools import cache
from speed2 import *
from itertools import *

A = -2
data = open("input/temp").read().splitlines()
data = open("input/2024/d21").read().splitlines()

def makeDict(grid):
    return {j : np.array([idx, jdx]) for idx, i in enumerate(grid) for jdx, j in enumerate(i)}
numPad = np.array([[7, 8, 9], [4, 5, 6], [1, 2, 3], [-1, 0, A]])
arrowPad = np.array([[' ', '^', 'A'], ['<', 'v', '>']])
# arrowPad = np.array([[-1, 0, A], [3, 2, 1]])

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
    # print(f'\tChecking path {p} starting at {s}: ({i}, {j})')
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
    # print(f'Navigating from {s} to {e} with {d}')
    paths = ["".join(p) for p in findPaths(d) if checkPath(s, p, numPad, -1 if numPad else ' ')]
    paths = sorted(paths, key = checkChanges, reverse=False)
    return paths

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

def selectBestPath(paths):
    return sorted(paths, key = scorePath, reverse=False)[0]

paths = []
scores = []
# data = data[-1:]
for i in data:
    paths.append(i)
    radRobo = ''
    cur = A
    for j in i:
        j = A if j == 'A' else int(j)
        ps = enterNumberFrom(cur, j)
        radRobo += selectBestPath(ps) + 'A'
        cur = j
    paths.append(radRobo)
    # print(radRobo)

    cur = 'A'
    frozRobo = ''
    for j in radRobo:
        frozRobo += enterNumberFrom(cur, j, 0)[0] + 'A'
        cur = j
    paths.append(frozRobo)
    # print(frozRobo)

    cur = 'A'
    us = ''
    for j in frozRobo:
        us += enterNumberFrom(cur, j, 0)[0] + 'A'
        cur = j
    scores.append((len(us) , int(i[:-1])))
    paths.append(us)

# for i in paths:
#     print(i)
print(scores)
print(sum([l * n for (l, n) in scores]))

@cache
def getArrowPresses(s):
    pass
