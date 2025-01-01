import numpy as np

file = 'temp.in'
file = 'd6.in'
data = open(file).read().splitlines()

times = ([int(i) for i in data[0].split()[1:]])
dist = ([int(i) for i in data[1].split()[1:]])

margins = []
for [t, d] in np.array([times, dist]).T:
    charges = np.arange(t)
    distances = charges * (t - charges)
    margins.append(np.sum(distances > d))
print(np.prod(margins[:-1]))
print(margins)
