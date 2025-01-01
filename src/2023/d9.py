import numpy as np

file = 'temp.in'
file = 'd9.in'
data = open(file).read().splitlines()
seqs = [np.array([int(i) for i in l.split()]) for l in data]

fins = []
starts = []
for s in seqs:
    temp = np.diff(s)
    diffs = [s, temp]
    while np.any(temp) != 0:
        diffs.append(temp := np.diff(temp))
    
    fins.append(sum([i[-1] for i in diffs]))
    
    #p2
    prev = 0
    for d in diffs[::-1]:
        prev = d[0] - prev
    starts.append(prev)
    
print(sum(fins))
print(sum(starts))