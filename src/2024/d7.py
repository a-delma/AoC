import numpy as np
from itertools import product 

data = open('input/temp').read().splitlines()
data = open('input/d7').read().splitlines()
data = [[[int(z) for z in y.strip().split(" ")] for y in x.split(":")] for x in data]

def testExample(x, ops):
    result = x[0][0]
    inputs = x[1]
    operands = product('ops', repeat=len(inputs) - 1) 
    for x in operands:
        total = inputs[0]
        for i, op in enumerate(x):
            if op == '*':
                total *= inputs[i + 1]
            elif op == '+':
                total += inputs[i + 1]
            else:
                total = int(f'{total}{inputs[i + 1]}')
        if total == result:
            return True
    return False

print(sum([x[0][0] for x in data if testExample(x, '+*')]))
print(sum([x[0][0] for x in data if testExample(x, '+*|')]))
# print(data)