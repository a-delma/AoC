import numpy as np

import sys
sys.setrecursionlimit(50_000)

file = 'temp.in'
# file = 'd12.in'
data = [l.split() for l in open(file).read().splitlines()]
rows = [np.array([c for c in l[0]], dtype=str) for l in data]
values = [[int(i) for i in l[1].split(',')] for l in data]

def solveRow(row, toPlace, succ, fail):
    if not toPlace:
        if np.any(row == '#'):
            fail()
        else:
            return succ(fail)
    elif row.size == 0:
        fail()
    else:
        l = toPlace[0]
        if len(row) < l:
            fail()
        else:
            match row[0]:
                case '.':
                    solveRow(row[1:], toPlace, succ, fail)
                case '#':
                    if np.all(np.isin(row[:l], ['#', '?'])) and (len(row) == l or row[l] == '.' or row[l] == '?'):
                        solveRow(row[l+1:], toPlace[1:], succ, fail)
                    else:
                        fail()
                case '?':
                    if np.all(np.isin(row[:l], ['#', '?'])) and (len(row) == l or row[l] == '.' or row[l] == '?'):
                        solveRow(row[l+1:], toPlace[1:], succ, lambda: (solveRow(row[1:], toPlace, succ, fail)))
                    else:
                        solveRow(row[1:], toPlace, succ, fail)

count = 0
def succ(fail):
    global count
    count += 1
    # print('Yatta')
    return fail
def fail():
    print(count)
    exit()
i = 1
# solveRow(rows[i], values[i], succ, lambda: print('fail'))
# print(count)
# exit()
for r, v in zip(rows, values):
    solveRow(r, v, succ, fail)
    # break
print(count)