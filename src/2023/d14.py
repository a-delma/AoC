import numpy as np
from functools import cache

ROUND, SQUARE, PATH = 'O', '#', '.'

file = 'temp.in'
file = 'd14.in'
data = open(file).read()

N = lambda s: np.array([[PATH if c == '.' else SQUARE if c == '#' else ROUND for c in l] for l in s.splitlines()])
S = lambda a: '\n'.join([''.join(l) for l in a])

def spinWrapper(data, num):
    copy = ''
    for i in range(num):
        data = fullSpin(data)
        if data == copy:
            break
        if fullSpin.cache_info().hits == 1:
            first, copy = i, data
    spinsLeft = (num - (first + 1)) % (i - first)
    for _ in range(spinsLeft):
        data = fullSpin(data)
    return N(data)

@cache
def fullSpin(data):
    for _ in range(4):
        data = spin(data)
        data = S(np.rot90(N(data), 3))
    return data

@cache
def spin(data):
    curState = N(data)
    prevState = np.zeros_like(curState)
    while not np.array_equal(prevState, curState):
        prevState = curState.copy()
        for ydx, y in enumerate(prevState):
            if ydx != 0:
                for xdx, x in enumerate(y):
                    if x == ROUND and curState[ydx-1, xdx] == PATH:
                        curState[ydx-1, xdx] = ROUND
                        curState[ydx, xdx] = PATH
    return S(curState)

# data = spinWrapper(data, 1000000000)
print(sum([(ydx + 1) * np.sum(y == ROUND) for ydx, y in enumerate(np.flip(spinWrapper(data, 1000000000), axis=0))]))