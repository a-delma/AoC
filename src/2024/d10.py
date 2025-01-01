import numpy as np

UP = [-1, 0]
RIGHT = [0, 1]
DOWN = [1, 0]
LEFT = [0, -1]
dirs = [UP, RIGHT, DOWN, LEFT]


data = open('input/temp').read().splitlines()
data = open('input/d10').read().splitlines()

data = np.array([[int(x) for x in y] for y in data])
heads = [(x, y) for x, y in zip(*np.where(data == 0))]

peaks = set()
peaks2 = 0

def explore(i, j, h):
    global peaks2
    for m, n in dirs:
        i2, j2 = i + m, j + n
        if 0 <= i2 < data.shape[0] and \
            0 <= j2 < data.shape[1] and \
                data[i2, j2] == h + 1:
                    if data[i2, j2] == 9:
                        peaks.add((i2, j2))
                        peaks2 += 1
                    else:
                        explore(i2, j2, h+1)
total = 0
total2 = 0
for [i, j] in heads:
    peaks = set()
    explore(i, j, 0)
    total += len(peaks)
print(total, peaks2)