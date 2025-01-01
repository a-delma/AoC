import numpy as np
import matplotlib.image

file = 'temp.in'
# file = 'd18.in'
data = np.array([l.split() for l in open(file).read().splitlines()])

height = np.array(data[data[:, 0] == 'D', 1], dtype=int).sum() * 2
width = np.array(data[data[:, 0] == 'R', 1], dtype=int).sum() * 2

grid = np.zeros((height, width), dtype=int)
y, x = height // 2, width // 2
y, x = 0,0
grid[y, x] = 1
for d, n, _ in data:
    n = int(n)
    match d:
        case 'U':
            grid[y-n:y+1, x] = 1
            y -= n
        case 'R':
            grid[y, x:x+n+1] = 1
            x += n
        case 'D':
            grid[y:y+n+1, x] = 1
            y += n
        case 'L':
            grid[y, x-n:x] = 1
            x -= n

# def fill_contours(arr):
#     return np.maximum.accumulate(arr,1) & \
#            np.maximum.accumulate(arr[:,::-1],1)[:,::-1]

# def fill_contours_fixed(arr):
#     return np.maximum.accumulate(arr, 1) &\
#            np.maximum.accumulate(arr[:, ::-1], 1)[:, ::-1] &\
#            np.maximum.accumulate(arr[::-1, :], 0)[::-1, :] &\
#            np.maximum.accumulate(arr, 0)
           
           
# def dumpGrid(g, file):
#     temp = np.zeros(g.shape, dtype=str)
#     temp[g == 1] = '#'
#     temp[g == 0] = ' '
#     with open(file, 'w') as f:
#         for d in temp:
#             if np.any(d == '#'):
#                 f.write(''.join(d) + '\n')

# dumpGrid(grid, 'outline.csv')
# dumpGrid(fill_contours_fixed(grid), 'fill.csv')
matplotlib.image.imsave('outline.png', grid)
