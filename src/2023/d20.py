import numpy as np
from collections import deque

import networkx as nx
import matplotlib.pyplot as plt

file = 'temp.in'
file = 'd20.in'
data = open(file).read().splitlines()


BROAD, FLIP, CONJ, BUTTON = 'broadcaster', '%', '&', 'button'
conjs = []
flips = []
modules = {}
queue = deque()
pulses = np.zeros((2), dtype=int)
count = 0

G = nx.DiGraph()

class Module():
    def __init__(self, d) -> None:
        d = d.split('->')
        if (temp := d[0].strip()) in [BROAD, BUTTON, 'rx']:
            self.type = temp
            self.name = temp
        else:
            self.name = d[0][1:-1] 
        self.targets = [l.strip() for l in (d[1].split(','))]
        modules[self.name] = self
        G.add_node(self.name)
        for t in self.targets:
            G.add_edge(self.name, t)
    
    def processNode(self, src, sig):
        global queue
        queue += [(self, 0, t) for t in self.targets]
    
    def __repr__(self) -> str:
        return f'<{self.name} {self.type}> -> {self.targets}'
    
class Flop(Module):
    def __init__(self, d) -> None:
        super().__init__(d)
        self.type = FLIP
        self.state = False
        flips.append(self)
        
    def processNode(self, src, sig):
        global queue
        if sig == 0:
            self.state = not self.state
            queue += [(self, int(self.state), t) for t in self.targets]
        
class Conj(Module):
    def __init__(self, d) -> None:
        super().__init__(d)
        self.type = CONJ
        self.state = {}
        conjs.append(self)
        self.status = []
        
    def registerSrc(self, src):
        self.state[src] = 0
        
    # def checkStatus(self):
    #     for i, v in self.state.items():
    #         if v == 0:
    #             self.status.append(count)
        
    def processNode(self, src, sig):
        global queue
        self.state[src] = sig
        if np.all(list(self.state.values())):
            queue += [(self, 0, t) for t in self.targets]
            self.status.append(count)
        else:
            queue += [(self, 1, t) for t in self.targets]

class Rx(Module):
    def __init__(self, d) -> None:
        super().__init__(d)
    
    def processNode(self, src, sig):
        # print([f'{i.name}:{int(i.state)}' for i in flips])
        # exit()
        if sig == 0:
            print(count)
            exit()
            
            
Module(f'{BUTTON} -> {BROAD}')
Rx(f'rx -> NULL')

for d in data:
    if d[0] == FLIP:
        Flop(d)
    elif d[0] == CONJ:
        Conj(d)
    else:
        Module(d)


for m in modules.values():
    for t in m.targets:
        if t in modules and type(modules[t]) is Conj:
            modules[t].registerSrc(m)

color_map=[]
for n in G.nodes:
    if n != 'NULL':
        t = type(modules[n])
        if t is Rx:
            color_map.append('red')
        elif t is Flop:
            color_map.append('blue')
        elif t is Conj:
            color_map.append('green')
        else:
            color_map.append('black')
    else:
        color_map.append('white')
        

# nx.draw(G, node_color=color_map, with_labels=True, pos=nx.fruchterman_reingold_layout(G))
# plt.show()
# exit()
# for _ in range(10):
#     queue.append((modules[BUTTON], 0, BROAD))
#     while queue:
#         (src, sig, tgt) = queue.popleft()
#         print(f'{src.name} -{sig}-> {tgt}')
#         pulses[sig] += 1
#         if tgt in modules:
#             modules[tgt].processNode(src, sig)
# print(pulses[0] * pulses[1])
            
while True:
    count += 1
    queue.append((modules[BUTTON], 0, BROAD))
    while queue:
        (src, sig, tgt) = queue.popleft()
        if tgt in modules:
            modules[tgt].processNode(src, sig)
    if count % 5000 == 0:
        print(count, end='|')
        print([f'{n}: {modules[n].status}' for n in ['pb', 'nl', 'rr', 'dj']])
        exit()
    
            
