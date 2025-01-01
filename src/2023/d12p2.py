import numpy as np
from functools import cache

data = [l.split() for l in open('d12.in').read().splitlines()]
rows = [np.array([c for c in l[0]], dtype=str) for l in data]
values = [[int(i) for i in l[1].split(',')] for l in data]

N, P = lambda x: ''.join(x.tolist()), lambda x: f'{x}'

values = [P(v+v+v+v+v) for v in values]
rows = [N(np.tile(np.pad(r, (0, 1), 'constant', constant_values='?'), 5)[:-1]) for r in rows]

@cache
def solveRow(row, toPlace):
    row, toPlace = np.array([r for r in row], dtype=str), eval(toPlace)
    if not toPlace:
        return 0 if np.any(row == '#') else 1
    elif row.size == 0:
        return 0
    else:
        l = toPlace[0]
        if len(row) < l:
            return 0
        else:
            match row[0]:
                case '.':
                    return solveRow(N(row[1:]), P(toPlace))
                case '#':
                    if np.all(np.isin(row[:l], ['#', '?'])) and (len(row) == l or row[l] == '.' or row[l] == '?'):
                        return solveRow(N(row[l+1:]), P(toPlace[1:]))
                    else:
                        return 0
                case '?':
                    if np.all(np.isin(row[:l], ['#', '?'])) and (len(row) == l or row[l] == '.' or row[l] == '?'):
                        return solveRow(N(row[l+1:]), P(toPlace[1:])) + solveRow(N(row[1:]), P(toPlace))
                    else:
                        return solveRow(N(row[1:]), P(toPlace))

print(sum([solveRow(r, v) for r, v in zip(rows, values)]))