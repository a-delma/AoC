import numpy as np

OBSTACLE = 8
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

data = open('input/temp').read().splitlines()
data = open('input/d6').read().splitlines()

data = np.array([[x for x in y] for y in data])
grid = np.zeros(data.shape, dtype=int)
obs  = np.zeros_like(data, dtype=int)

for idx, i in enumerate(data):
    for jdx, j in enumerate(i):
        if j == '^':
            guard_start = (idx, jdx)
            face = 0
        elif j == '#':
            obs[idx, jdx] = OBSTACLE

def move(g, f):
    match f:
        case 0:
            return g[0] - 1, g[1]
        case 1:
            return g[0], g[1] + 1
        case 2:
            return g[0] + 1, g[1]
        case 3:
            return g[0], g[1] - 1
guard = guard_start
grid[guard] = 1
while True:
    try:
        newPos = move(guard, face)
        if obs[newPos] == OBSTACLE:
            face = (face + 1) % 4
        else:
            guard = newPos
            grid[guard] = 1
    except IndexError:
        break
    
grid2 = np.zeros((grid.shape + (4,)))
total = 0
indices = list(zip(*np.where(grid == 1)))
for c, (i, j) in enumerate(indices):
    print(f'Placing OBS at {i, j}: ({c} : {len(indices)})')
    if (i, j) is not guard_start:
        obs[i, j] = OBSTACLE
        grid2[:,:,:] = 0
        guard = guard_start
        face = 0
        while True:
            newPos = move(guard, face)
            if newPos[0] < 0 or newPos[0] >= grid.shape[0] or \
                newPos[1] < 0 or newPos[1] >= grid.shape[1]:
                break 
            if obs[newPos] == OBSTACLE:
                face = (face + 1) % 4
            elif grid2[guard + (face, )] == 1:
                total += 1
                break
            else:
                grid2[guard + (face, )] = 1
                guard = newPos
    obs[i, j] = 0
    
print(np.sum(grid != 0))
print(total)