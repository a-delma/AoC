import numpy as np
from itertools import chain, zip_longest

data = open('input/temp').read()
data = open('input/d9').read()
dataSeqs = data[::2]
blanks   = data[1::2]

flatten = lambda xss: [x for xs in xss for x in xs]
makeSub = lambda x: [-1 for y in range(int(x)) ] if int(x) != 0 else []

newData = [[i for y in range(int(x))] for i, x in enumerate(dataSeqs)]
blankList  = [makeSub(x) for x in blanks]
disk = flatten([x + y for (x, y) in (zip_longest(newData, blankList, fillvalue=[]))])


# print(disk)
notDone = True
while -1 in disk and notDone:
    while (x := disk.pop()) != -1:
        if -1 in disk:
            disk[disk.index(-1)] = x
        else:
            disk += [x]
            notDone = True
            break

# print(sum(i * x for i, x in enumerate(disk)))
  
def printList(x):
    string = ''
    for (f, l, d) in x:
        if f:
            string += ''.join([str(d) for _ in range(l)])
        else:
            string += ''.join(['.' for _ in range(l)])
    return string
  
disk2 = [(i % 2 == 0, int(x), i//2) for i, x in enumerate(data)]

lastIndex = len(disk2) - 1
while lastIndex != 0:
    printList(disk2)
    # print(disk2)
    tR = disk2[lastIndex]
    if tR[0]:
        # print(tR, lastIndex)
        for i, (f, l, _) in enumerate(disk2[:lastIndex]):
            if not f and l >= tR[1]:
                # print(f, l, _)
                disk2[lastIndex] = (False, tR[1], 0)
                disk2.insert(i, tR)
                disk2[i + 1] = (f, l - tR[1], 0)
                break
    lastIndex -= 1

def sumList(x):
    arr = []
    for (f, l, d) in x:
        if f:
            arr += [d for _ in range(l)]
        else:
            arr += [0 for _ in range(l)]
    return arr


print(sum([x * i for i, x in enumerate(sumList(disk2))]))