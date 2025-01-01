import numpy as np
import pandas as pd
from math import lcm

file = 'temp.in'
file = 'd8.in'
data = open(file).read().split('\n\n')
    
dirs = [(lambda x: 0 if x == 'L' else 1)(l) for l in data[0]]
nodeStrs = map(lambda x: x.split(' = '), data[1].splitlines())
nodes = {}
for n in nodeStrs:
    nodes[n[0]] = n[1][1:-1].split(', ')
    
curNode = 'AAA'
count = 0
while curNode != 'ZZZ':
    curNode = nodes[curNode][dirs[count % len(dirs)]]
    count += 1
print(count)
    
# p2
indexNodes = (list(filter(lambda x: x[2] == 'A',nodes.keys())))
dests = (list(filter(lambda x: x[2] == 'Z',nodes.keys())))

count = 0
results = []
stillSingle = True
while indexNodes:
    indexNodes = ([nodes[n][dirs[count % len(dirs)]] for n in indexNodes])
    count += 1
    for n in indexNodes:
        if n in dests:
            results.append(count)
            indexNodes.remove(n)
            
    # curNode = nodes[curNode][dirs[count % len(dirs)]]
print(lcm(*results))