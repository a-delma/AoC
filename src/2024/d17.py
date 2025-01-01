import numpy as np
from speed import *
import re
import itertools

data = open('input/temp').read().split('\n\n')
data = open('input/d17').read().split('\n\n')

A, B, C = [int(re.findall(r'\d+', x)[0]) for x in data[0].splitlines()]
ops  = ([int(x) for x in re.findall(r'\d+', data[1])])

def runProgram(A, B, C, ops):
    def lookup(v):
        match v:
            case 4:
                return A
            case 5:
                return B
            case 6:
                return C
            case 7:
                raise IndexError
            case _:
                return v
    pnt = 0
    out = []
    while pnt < len(ops):
        a, b, c = [bin(x) for x in [A, B, C]]
        o, v = ops[pnt:pnt + 2]
        match o:
            case 0: # ADV
                v = lookup(v)
                A = A // (2 ** v)
            case 1: # bxl
                B = B ^ v
            case 2: # bst
                v = lookup(v)
                B = v % 8
            case 3: # jnz
                if A != 0:
                    pnt = v
                    continue
            case 4: # bxc
                B = B ^ C
            case 5: # out
                v = lookup(v) % 8
                out.append(v)
            case 6: # bdv
                v = lookup(v)
                B = A // (2 ** v)
            case 7: # cdv
                v = lookup(v)
                C = A // (2 ** v)
        pnt += 2
    return out

def convert(l):
    return int(''.join([f'{x:03b}' for x in l]),2)

def getTemplate(l):
    t = {}
    arrs = [list(x) for x in itertools.product(range(8), repeat=l)]
    for i in arrs:
        out = runProgram(convert(i), B, C, ops)
        # print(i, out)
        out = tuple(reversed(out))
        t[out[-1]] = t.get(out[-1], []) + [i]
    return t

validSolutions = []
def findMatch(left, sol):
    if not left:
        validSolutions.append(sol)
        return
    op = left.pop()
    temp = templates[op]
    for i in temp:
        match len(sol):
            case 0:
                findMatch(left[:], i)
            case _:
                if sol[-3:] == i[:3]:
                    findMatch(left[:], sol + [i[-1]])
            
if __name__ == '__main__':
    out = runProgram(A, B, C, ops)
    print(','.join([str(x) for x in out]))
    templates = getTemplate(4)
    findMatch(ops[:], [])
    print(min([convert(x) for x in validSolutions]))
