import numpy as np

file = 'temp.in'
file = 'd15.in'
data = open(file).read().split(',')

def hassssh(sssss):
    total = 0
    for s in sssss:
        total += ord(s)
        total *= 17
        total = total % 256
    return total

boxes = {}

for s in data:
    if '=' in s:
        s = s.split('=')
        boxNum = hassssh(s[0])
        lenlen = s[1]
        if boxNum not in boxes:
            boxes[boxNum] = np.array([[s[0], lenlen]])
        else:
            box = boxes[boxNum]
            place = np.where(box[:, 0] == s[0])[0]
            if place.shape[0] != 0:
                box[place, 1] = lenlen
            else:
                boxes[boxNum] = np.vstack((box, [s[0], lenlen]))
    else:
        boxNum = hassssh(s[:-1])
        if boxNum in boxes:
            box = boxes[boxNum]
            place = np.where(box[:, 0] == s[:-1])[0]
            if place.shape[0] != 0:
                boxes[boxNum] = np.delete(box, place, axis=0)
                
print(sum([((key + 1) * np.array([(idx + 1) * int(x[1]) for idx, x in enumerate(box)])).sum() for key, box in boxes.items() if box.shape[0] > 0]))
