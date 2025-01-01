import os

nextDay = max([int(x[1:-3]) for x in os.listdir('.') if x[0] == 'd']) + 1

with open(f'd{nextDay}.py', '+w') as f:
    f.write('import numpy as np\n')
    f.write('from speed import *\n\n')
    f.write(f"data = open('input/temp').read().splitlines()\n")
    f.write(f"# data = open('input/d{nextDay}').read().splitlines()\n")
    f.write('print(data)')
    
open(f'input/d{nextDay}', 'a').close()