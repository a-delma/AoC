import numpy as np
import matplotlib.image

def remap(l):
    _, _, h = l.split()
    match h[-2]:
        case '0':
            d = 'R'
        case '1':
            d = 'D'
        case '2':
            d = 'L'
        case '3':
            d = 'U'
        case _:
            print('hello')    
    h = (eval(f'0x{h[2:-2]}'))
    return [d, h, 0]
    
file = 'temp.in'
file = 'd18.in'
data = np.array([remap(l) for l in open(file).read().splitlines()])
# data = np.array([l.split() for l in open(file).read().splitlines()])
print(data)

y, x = 0, 0
points = [(x,y)]
boundary = 0
for d, n, _ in data:
    n = int(n)
    match d:
        case 'U':
            y -= n
        case 'R':
            x += n
        case 'D':
            y += n
        case 'L':
            x -= n
    boundary += n
    points.append((x,y))

def area(p):
    return 0.5 * abs(sum(x0*y1 - x1*y0
                         for ((x0, y0), (x1, y1)) in segments(p)))

def segments(p):
    return zip(p, p[1:] + [p[0]])

# def area_np(x, y):        
#     x = np.asanyarray(x)
#     y = np.asanyarray(y)
#     n = x.size
#     shift_up = np.arange(-n+1, 1)
#     shift_down = np.arange(-1, n-1)    
#     return (x * (y.take(shift_up) - y.take(shift_down))).sum() / 2.0

# def PolyArea(x,y):
#     return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))

# def Area(corners):
#     n = len(corners) # of corners
#     area = 0.0
#     for i in range(n):
#         j = (i + 1) % n
#         area += corners[i][0] * corners[j][1]
#         area -= corners[j][0] * corners[i][1]
#     area = abs(area) / 2.0
#     return area

# xs = [x for x, y in points]
# ys = [y for x, y in points]
a = area(points) + 1
interior = a - boundary / 2
print(interior + boundary)