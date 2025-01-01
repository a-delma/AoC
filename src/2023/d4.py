import numpy as np

file = 'temp.in'
file = 'd4.in'
data = open(file).read().splitlines()
lines = [l.split(':')[1] for l in data]
lines = [l.split('|') for l in lines]

total = 0
numCards = len(lines)
cards = {}

for idx, l in enumerate(lines):
    idx += 1
    winning = set([int(g) for g in l[0].split()])
    myNums = set([int(g) for g in l[1].split()])
    
    matches = winning.intersection(myNums)
    if len(matches) > 0:
        total += 2 ** (len(matches) - 1)
    cards[idx] = [idx + l + 1 for l in range(len(matches)) if idx + l + 1 <= numCards]
    
stockpile = list(np.arange(numCards) + 1)
counter = 0
while len(stockpile) > 0:
    card = stockpile.pop()
    counter += 1
    stockpile += (cards[card])

print(total)
print(counter)