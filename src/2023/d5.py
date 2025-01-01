import numpy as np
from multiprocessing import pool

file = 'temp.in'
file = 'd5.in'
data = open(file).read().split('\n\n')

seeds = np.array([int(i) for i in data[0].split(':')[1].split()])

def parseMap(data):
    data = data.splitlines()[1:]
    mapping = []
    for l in data:
        [d, s, r] = map(int, l.split())
        mapping.append((s, s + r, d))
    return mapping
    
def lookup(key, mapping):
    for [s, e, d] in mapping:
        if key >= s and key < e:
            return d + (key - s)
    return key
    
mappings = [parseMap(i) for i in data[1:]]

locs = []

for s in seeds:
    temp = s
    for m in mappings:
        temp = lookup(temp, m)
    locs.append(temp)
    
print(locs)
print(min(locs))

print('------')

smallest = min(locs) * 2
sRanges = seeds.reshape((-1, 2))

print(sRanges[:, 1].sum())

for [s, r] in sRanges:
    for i in range(s, s + r):
        temp = i
        for m in mappings:
            # print(temp)
            temp = lookup(temp, m)
        # print(f'Seed: {i}, Location: {temp}')
        smallest = min(smallest, temp)
    print(smallest)
        
print(smallest)