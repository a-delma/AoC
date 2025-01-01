import numpy as np
from functools import cache

data = open('input/temp').read()
data = open('input/d11').read()

data = [int(x) for x in data.split(' ')]

@cache
def update_cache(x, u):
    if u == 0:
        return 1
    if x == 0:
        return update_cache(1, u - 1)
    elif len(str(x)) % 2 == 0:
        s = str(x)
        return update_cache(int(s[:len(s)//2]), u - 1) + update_cache(int(s[len(s)//2:]), u - 1) 
    else:
        return update_cache(x * 2024, u - 1)
    
print(sum([update_cache(x, 25) for x in data]))
print(sum([update_cache(x, 75) for x in data]))