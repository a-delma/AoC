import numpy as np

data = open('input/temp').read().splitlines()
# data = open('input/d12').read().splitlines()

data = np.array([[x for x in y] for y in data])

regions = []
for i in data:
    for j in i:
        region = j
        
        
