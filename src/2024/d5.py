import numpy as np
from functools import cmp_to_key

data = [x.splitlines() for x in open('input/d5').read().split('\n\n')]

orderings = [[int(y) for y in x.split('|')] for x in data[0]]
updates   = [np.array([int(y) for y in x.split(',')]) for x in data[1]]

rules = {}
for (x, y) in orderings:
    values = rules.get(x, [])
    values.append(y)
    rules[x] = values

checkUpdate = lambda u: np.all([not np.any(np.isin(u[:idx], rules.get(i, []))) for idx, i in enumerate(u)])
cmp = lambda x, y : -1 if np.any(rules.get(x, []) == y) else (1 if np.any(rules.get(y, []) == x) else 0)

fixedUpdates = [sorted(x, key=cmp_to_key(cmp)) for x in updates if not checkUpdate(x)]

print(sum([x[len(x) // 2] for x in updates if checkUpdate(x)]))
print(sum([x[len(x) // 2] for x in fixedUpdates]))