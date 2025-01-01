import numpy as np
import re
from speed import *
from math import prod

data = open('input/temp').read().splitlines()
data = open('input/d14').read().splitlines()
data = [[int(y) for y in re.findall(r'-?\d+', x)] for x in data]

# width by height
# y, x :(
b = [7, 11]
b = [103, 101]

def move(r, n):
    v = np.array(r[2:])
    p = np.array(r[:2])
    vn = v * n
    x, y = p + vn
    return x % (b[1]), y % (b[0])

steps = [move(x, 100) for x in data]
board = np.zeros((b), dtype=int)
for (x, y) in steps:
    board[y, x] += 1
    
Q1 = board[:b[0] // 2,:b[1] // 2]
Q2 = board[:b[0] // 2,b[1] // 2 + 1:]
Q3 = board[b[0] // 2 + 1:,:b[1] // 2]
Q4 = board[b[0] // 2 + 1:, b[1] // 2 + 1:]

print(prod([np.sum(x) for x in [Q1, Q2, Q3, Q4]]))

def printBoard(x):
    def mapI(y):
        return ' ' if y == 0 else 'X'
    
    for r in x:
        l = "".join([mapI(i) for i in r])
        print(l)

for i in range(1000):
    steps = [move(x, 28 + i * 101) for x in data]
    board = np.zeros((b), dtype=int)
    for (x, y) in steps:
        board[y, x] += 1
    print(f'\n\n\nAfter {10 + i * 101} Steps')
    printBoard(board)