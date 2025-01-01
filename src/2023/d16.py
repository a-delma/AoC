import numpy as np

UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3

file = 'temp.in'
file = 'd16.in'
data = np.array([[c for c in l] for l in open(file).read().splitlines()])

def sendBeam(b):
    beams = [b]
    energy = np.full_like(data, False)
    tiles = set()
    while beams:
        beam = beams.pop()
        while 0 <= beam[0] < data.shape[0] and 0 <= beam[1] < data.shape[1] and tuple(beam) not in tiles:
            energy[beam[0], beam[1]] = '#'
            tiles.add(tuple(beam))
            match data[beam[0], beam[1]]:
                case '|':
                    if beam[2] in [RIGHT, LEFT]:
                        beam[2] = DOWN
                        beams.append([beam[0], beam[1], UP])
                case '-':
                    if beam[2] in [UP, DOWN]:
                        beam[2] = RIGHT
                        beams.append([beam[0], beam[1], LEFT])  
                case '\\':
                    beam[2] = DOWN if (d := beam[2]) == RIGHT else (
                            LEFT if d == UP else (
                            RIGHT  if d == DOWN else UP))
                case '/':
                    beam[2] = UP if (d := beam[2]) == RIGHT else (
                            RIGHT if d == UP else (
                            LEFT  if d == DOWN else DOWN))
            match beam[2]:
                case 0:
                    beam[0] -= 1
                case 1:
                    beam[1] += 1
                case 2:
                    beam[0] += 1
                case 3:
                    beam[1] -= 1
    return((energy == '#').sum())      
    
print(sendBeam([0, 0, RIGHT]))

sums = []
for y in range(data.shape[0]):
    sums.append(sendBeam([y, 0, RIGHT]))
    sums.append(sendBeam([y, data.shape[1] - 1, LEFT]))

for x in range(data.shape[1]):
    sums.append(sendBeam([0, x, DOWN]))
    sums.append(sendBeam([data.shape[0] - 1, x, UP]))
    
print(max(sums))