import numpy as np

[l1, l2] = [np.array(sorted(z)) for z in zip(*[[int(y) for y in x.split()] for x in open('input/d1').read().splitlines()])]

print(sum([abs(x - y) for (x, y) in zip(l1, l2)]))
print(sum(l1 * np.array([np.sum(l2 == x) for x in l1])))
