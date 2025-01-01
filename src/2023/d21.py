import numpy as np
from scipy.signal import convolve

HEDGE = '#'

file = 'temp.in'
file = 'd21.in'
data = np.array([[c for c in l] for l in open(file).read().splitlines()])
grid = np.zeros_like(data, dtype=int)


def drawPlot():
    for ydx, y in enumerate(data):
        line = ''
        for xdx, x in enumerate(y):
            line += ('   S' if x == 'S' else ('   #' if x == '#' else f'{grid[ydx, xdx]:4d}'))
        print(line)


kernel = np.zeros((3, 3), dtype=int)
kernel[0, 1] = 1
kernel[2, 1] = 1
kernel[1, 0] = 1
kernel[1, 2] = 1

curRow = grid.copy()
# curRow[data == 'S'] = 1
curRow[0, 0] = 1
# curRow[0, 0]  
# for i in range(64):
#     curRow = convolve(curRow, kernel, mode='same')
#     curRow[curRow >= 1] = 1
#     curRow[data == '#'] = 0
#     curRow[grid != 0] = 0
#     grid[curRow == 1] = i + 1

count = 0
while True:
    curRow = convolve(curRow, kernel, mode='same')
    curRow[curRow >= 1] = 1
    curRow[data == '#'] = 0
    curRow[grid != 0] = 0
    grid[curRow == 1] = count + 1
    count += 1
    if curRow.sum() == 0:
        break
drawPlot()

# print(np.logical_and(grid % 2 == 0, grid > 0).sum())