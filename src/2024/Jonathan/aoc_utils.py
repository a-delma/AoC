# Inspired by https://github.com/nthistle/advent-of-code/blob/master/2022/day14/aoc_tools.py
import re
import math
import numpy as np
# from pulp import *
# from z3 import *
# from collections import Counter
# from functools import cache
# import sys
# sys.setrecursionlimit(100000)


"""-----
Template
--------

from aoc_utils import *
import numpy as np
from functools import cache
# import sys
# sys.setrecursionlimit(150000)

def main(filename):
    with open(filename) as file:
        # arr = np.array([[int(c) for c in  s] for s in file.read().split("\n")])
        # arrs = [np.array([[int(c) for c in  s] for s in arr]) for arr in file.read().split("\n\n")]
        lines = file.read().split("\n")

if __name__ == "__main__":
    filename = "Input/test.txt"
    # filename = "Input/day-xx.txt"
    main(filename)
"""

# Extracts all (+ or -) integers from a string
def nums(s):
    m = re.findall("-?\d+", s)
    return [int(x) for x in m]

# Returns True iff (y,x) is in bounds of the array
def in_bound(y, x, arr):
    return y >= 0 and y < len(arr) and x >= 0 and x < len(arr[0])


# Converts 2D arrays to human-readable string, and back (while preserving shape)
def arr2str(arr):
    return " ".join(["".join(row) for row in arr])

def str2arr(s):
    return np.array([[c for c in row] for row in s.split(" ")])

# Common Lp norms/distance functions
def l1_dist(p1, p2 = None):
    if p2 is None:
        p2 = [0 for _ in p1]
    return sum(abs(x1 - x2) for (x1, x2) in zip(p1, p2))

def l2_dist(p1, p2 = None):
    if p2 is None:
        p2 = [0 for _ in p1]
    return math.sqrt(sum(abs(x1 - x2)**2 for (x1, x2) in zip(p1, p2)))

def linf_dist(p1, p2 = None):
    if p2 is None:
        p2 = [0 for _ in p1]
    return max(abs(x1 - x2) for (x1, x2) in zip(p1, p2))

# Functions for working with collections of half-open intervals.
# Intervals of integers are in the form [lo, hi)
def count_union(intervals, within_range = None):
    if intervals is None or len(intervals) == 0:
        return 0

    if within_range is None:
        within_range = [min([x[0] for x in intervals]), max([x[1] for x in intervals])]

    sorted_intervals = sorted(intervals, key = lambda x : x[0])
    total = 0
    x = within_range[0]
    for (lo, hi) in sorted_intervals:
        if x < lo:
            x = lo
        if x < hi:
            total += min(hi, within_range[1]) - x
            x = hi
        if x >= within_range[1]:
            break
    return total

def get_union(intervals, within_range = None):
    lo = min(interval[0] for interval in intervals)
    hi = max(interval[1] for interval in intervals)
    if within_range is None:
        within_range = [lo, hi]
    inside = lambda x : np.any([curr_lo <= x < curr_hi
        and within_range[0] <= x < within_range[1]
        for (curr_lo, curr_hi) in intervals])
    return [x for x in range(lo, hi) if inside(x)]

"""A reminder of how to use z3
------------------------------
Variables:
- x = Int("x")
- y = Real("y")

s = Solver()
s.add(x < 10)

Additional Constraints:
- Sum([...])
- List comprehension

Logic:
- And(c1, ...)
- Or(c1, ...)
- If(x >= 0, x, -x)

Solve:
- s.check()
- m = s.model() is dictionary, where keys are vars
"""

####

"""A reminder of how to solve (I)LPs
Variables:
- LpVariable("name", cat = ["Binary" or "Integer"])

Constraints:
- lpSum([vars])
- lpDot([weights], [vars])
"""