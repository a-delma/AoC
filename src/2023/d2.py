import numpy as np

intialSet = {'green' : 13, 'blue' : 14, 'red' : 12}

file = 'temp.in'
file = 'd2.in'
lines = [l.split(':')[1] for l in open(file).read().splitlines()]
lines = [l.split(';') for l in lines]
lines = list(map(lambda x: [l.split(',') for l in x], lines))

total = 0
power = 0
for idx, game in enumerate(lines):
    cs = {'green' : 0, 'blue' : 0, 'red' : 0}
    g, b, r = 0, 0, 0
    for draw in game:
        for st in draw:
            [num, color] = st.split()
            cs[color] = max(int(num), cs[color])
    valid = True
    for init, this in zip(intialSet.values(), cs.values()):
        if this > init:
            valid = False
    if valid:
        total += idx + 1
    power += cs['green'] * cs['blue'] * cs['red']

print(total)
print(power)