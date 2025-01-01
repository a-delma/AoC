import numpy as np
from speed import *

BOX = 'O'
WALL = '#'
ROBO = '@'

UP = [-1, 0]
RIGHT = [0, 1]
DOWN  = [1, 0]
LEFT  = [0, -1]

D = {'^' : UP, '>' : RIGHT, 'v' : DOWN, '<' : LEFT}

data = open('input/temp').read().split('\n\n')
data = open('input/d15').read().split('\n\n')

m = data[0]
m = m.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.')

grid = np.array([[y for y in x] for x in m.splitlines()])
inst = data[1].replace('\n', '')

robo  = np.array(next(zip(*np.where(grid == ROBO))))
toMove = []
def moveBox(p, d):
    [x, y] = p + d
    p = tuple(p)
    cur = grid[p]
    if cur == '.':
        return True
    elif cur == WALL:
        return False
    if d[0]: # moving vertically
        if cur == ']':
            ot = [x, y - 1]
        else:
            ot = [x, y + 1]
            p = tuple([p[0], p[1] + 1])
        if moveBox(np.array([x, y]), d) and moveBox(np.array(ot), d):
            toMove.append(p)
            return True
        else:
            return False
    else:
        nextSpace = grid[x, y]
        match nextSpace:
            case '#':
                return False
            case '.':
                grid[x, y] = grid[p]
                grid[p] = '.'
                return True
            case _:
                if moveBox(np.array([x, y]), d):
                    grid[x, y] = grid[p]
                    grid[p] = '.'
                    return True
                else:
                    return False

printArrayWithIndices(grid, 1)

for i in inst:
    toMove = []
    robo = np.array(robo)
    d = D[i]
    [x, y] = robo + d
    p = tuple(robo)
    nextSpace = grid[x, y]
    match nextSpace:
        case '#':
            continue
        case '.':
            grid[x, y] = grid[p]
            grid[p] = '.'
            robo = [x, y]
        case _:
            if moveBox(np.array([x, y]), d):
                if toMove:
                    if d == DOWN:
                        toMove.sort(key=lambda x: x[0], reverse=True)
                    else:
                        toMove.sort(key=lambda x: x[0], reverse=False)
                    for [idx, jdx] in toMove:
                        grid[tuple(np.array([idx, jdx]) + d)] = ']'
                        grid[tuple(np.array([idx, jdx - 1]) + d)] = '['
                        grid[idx, jdx] = '.'
                        grid[idx, jdx - 1] = '.'
                grid[x, y] = grid[p]
                grid[p] = '.'
                robo = [x, y]
    # printArrayWithIndices(grid, 1)
    # printArrayWithIndices(grid)


boxes = zip(*np.where(grid == '['))
print(sum([100 * i + j for (i, j) in boxes]))
    