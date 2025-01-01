from functools import cache

data = open('input/d19').read().split('\n\n')
tows = [x.strip() for x in data[0].split(',')]
outputs = data[1].splitlines()

@cache
def checkPossible(x):
    return 1 if x == '' else sum(checkPossible(x[len(t):]) for t in tows if x[:len(t)] == t)

print(sum(1 for x in outputs if checkPossible(x) > 0))
print(sum(checkPossible(x) for x in outputs))