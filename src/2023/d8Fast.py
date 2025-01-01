import numpy as np
import torch as tf
import time
tf.set_default_device('cuda')

file = 'temp.in'
file = 'd8.in'
data = open(file).read().split('\n\n')

dirs = [(lambda x: 0 if x == 'L' else 1)(l) for l in data[0]]
nodeStrs = list(map(lambda x: x.split(' = '), data[1].splitlines()))
nodes = {n[0] : idx for idx, n in enumerate(nodeStrs)}

graph = tf.zeros((2, len(nodes), len(nodes)))


for n in nodeStrs:
    [l, r] = n[1][1:-1].split(', ')
    n = n[0]
    graph[0, nodes[n], nodes[l]] = 1
    graph[1, nodes[n], nodes[r]] = 1
    
curNode = tf.zeros(len(nodes))
curNode[nodes['AAA']] = 1
dest = tf.zeros_like(curNode)
dest[nodes['ZZZ']] = 1
count = 0
while not tf.equal(curNode, dest):
    curNode = tf.matmul(curNode, graph[dirs[count % len(dirs)]])
    count += 1
print(count)


srcs = np.array(list(filter(lambda x: x[2] == 'A',nodes.keys())))
dests = np.array(list(filter(lambda x: x[2] == 'Z',nodes.keys())))
curNode = tf.zeros(len(nodes))
indices = [(nodes[s]) for s in srcs]
curNode[indices] = 1

destNodes = tf.zeros(len(nodes))
indices = [(nodes[s]) for s in dests]
destNodes[indices] = 1
count = 0

start = time.time()
while not tf.equal(curNode, destNodes):
    curNode = tf.matmul(curNode, graph[dirs[count % len(dirs)]])
    count += 1
    if count % 100000 == 0:
        end = time.time()
        print(f'{count}: {end - start}')

print(end - start)
print(count)