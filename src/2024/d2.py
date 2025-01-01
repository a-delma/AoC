import numpy as np

data = ([np.array([int(x) for x in y.split()]) for y in open('input/d2').read().splitlines()])

safe = lambda x: (np.all((diffs := np.diff(x)) > 0) or np.all(diffs < 0)) and (np.all(abs(diffs) >= 1) and np.all(abs(diffs) <= 3))
safe2 = lambda x: True if safe(x) else np.any([safe(np.delete(x, i)) for i in range(len(x))])
            
print(sum([int(safe(x)) for x in data]))
print(sum([int(safe2(x)) for x in data]))