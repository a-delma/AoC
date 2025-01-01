import numpy as np
from scipy.optimize import linprog
import re
from z3 import Int, Optimize, sat

data = open('input/temp').read().split('\n\n')
data = open('input/d13').read().split('\n\n')

data = [x.splitlines() for x in data]

def process(x):
    pattern = r'(\d+)'
    a = [int(x) for x in re.findall(pattern, x[0])]
    b = [int(x) for x in re.findall(pattern, x[1])]
    # p = [int(x) for x in re.findall(pattern, x[2])]
    p = [int(x) + 10000000000000 for x in re.findall(pattern, x[2])]
    return (a, b, p)

def solve2(x):
    A, B, target = x
    x = Int('x')
    y = Int('y')

    opt = Optimize()
    opt.add(x * A[0] + y * B[0] == target[0])
    opt.add(x * A[1] + y * B[1] == target[1])
    opt.add(x >= 0, y >= 0)

    opt.minimize(3 * x + y)

    if opt.check() == sat:
        model = opt.model()
        solution = {
            'x': model[x].as_long(),
            'y': model[y].as_long(),
            'cost': 3 * model[x].as_long() + model[y].as_long()
        }
        return solution['cost']
    else:
        return 0

def solveNp(x):
    a, b, p = x 
    A_eq = np.vstack([a, b]).T.astype(np.longdouble)
    p = np.array(p, dtype=np.longdouble)
    
    sol = np.linalg.solve(A_eq, p)
    print(sol)

def solveMach(x):
    a, b, p = x
    A_eq = np.vstack([a, b]).T
    c = [3, 1]
    b_eq = p
    result = linprog(c, A_eq=A_eq, b_eq=b_eq,bounds=(0, None), method='highs', integrality=[1, 1])
    
    if result.success:
        return int(3 * result.x[0] + result.x[1])
    else:
        return 0

machines = [process(x) for x in data]
solveNp(machines[1])
print(sum([solve2(x) for x in machines]))