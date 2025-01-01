import numpy as np
import pandas as pd
from functools import cmp_to_key

file = 'temp.in'
file = 'message.txt'
data = open(file).read().splitlines()

values = np.array(['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'])
mapping = np.arange(values.shape[0])
mapping = {v : m for (m, v) in zip(np.flip(mapping), values)}

bids = [int(l.split()[1]) for l in data]
hands = [[mapping[k] for k in l.split()[0]] for l in data]


def compareHand(hand1, hand2):
    # print(f'Comparing {h1} to {h2}')
    h1, _ = hand1
    h2, _ = hand2
    for l, r in zip(h1, h2):
        if h1 > h2:
            return 1
        elif h2 > h1:
            return -1
    return 0

tiers = {i : [] for i in range(7)}

def classifyHand(h1):
    h, _ = h1
    counts = pd.Series(h).value_counts()
    match counts.max():
        case 5:
            tiers[6].append(h1)
        case 4:
            tiers[5].append(h1)
        case 3:
            if counts.min() == 2:
                tiers[4].append(h1)
            else:
                tiers[3].append(h1)
        case 2:
            if len(counts) == 3:
                tiers[2].append(h1)
            else:
                tiers[1].append(h1)
        case _:
            tiers[0].append(h1)
        


for bid, hand in zip(bids, hands):
    classifyHand((hand, bid))
    
total = []
for t, hs in tiers.items():
    newList = sorted(hs, key=cmp_to_key(compareHand), reverse=False)
    tiers[t] = newList
    total += (newList)
    
# print(total)
print(sum([(idx + 1) * b for idx, (_, b) in enumerate(total)]))