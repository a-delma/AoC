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
# data = open('input/d15').read().split('\n\n')

grid = np.array([[y for y in x] for x in data[0].splitlines()])
inst = data[1].replace('\n', '')

walls = np.where(grid == WALL)
boxes = np.where(grid == BOX)
robo  = np.array(next(zip(*np.where(grid == ROBO))))

# def printBoard():
#     b = np.zeros_like(grid)
#     b[boxes] = BOX
#     b[walls] = WALL
#     b[tuple(robo)]  = ROBO
#     printArrayWithIndices(b)
    
def moveBox(p, d):
    # print(p, d)
    [x, y] = p + d
    p = tuple(p)
    # print(f'Moving {grid[p]} from {p} to: {x, y} {d}')
    nextSpace = grid[x, y]
    match nextSpace:
        case '#':
            return False
        case 'O':
            if moveBox(np.array([x, y]), d):
                grid[x, y] = grid[p]
                grid[p] = '.'
                return True
            else:
                return False
        case '.':
            grid[x, y] = grid[p]
            grid[p] = '.'
            return True

# printArrayWithIndices(grid)

for i in inst:
    d = D[i]
    if moveBox(robo, d):
        robo = robo + d
    # printArrayWithIndices(grid)
    
boxes = zip(*np.where(grid == BOX))
print(sum([100 * i + j for (i, j) in boxes]))
    