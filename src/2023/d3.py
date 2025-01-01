import numpy as np

file = 'temp.in'
# file = 'd3.in'
data = open(file).read().splitlines()
lines = [list(l) for l in data]
array = np.array(lines) 
array = np.pad(array, 1, 'constant', constant_values='.') # loads file into np array with extra padding to allow back indexing easily

numeric = np.isin(array, [str(l) for l in np.arange(10)]) # boolean array of numerals
periods = np.isin(array, ['.'])                           # boolean array of periods
syms    = np.logical_not(np.logical_or(numeric, periods)) # boolean array of non periods or numbers
gears   = np.isin(array, ['*'])                           # boolean array of asterics

# here we are looking at the difference of each element from the last, so when there is a change it becomes true
# argwhere returns the index of it giving coordinates like [1 0], [1 3], ...
sequences = np.argwhere(np.diff(numeric))
# since we know the index mark the start and stop, if we take them two at a time, ie reshaping a 2n x 2 into a n x 4
#   we then have rows of sequences of numbers, but the 3rd value is repetitive of the row, and the 2nd column is off by one 
numbers = sequences.reshape((-1, 4))[:, [0, 1, 3]]
numbers[:, 1] += 1
# now we have array with rows like [y x1 x2]

# returns true if any region around a number contains a symbol
def checkPart(x1, x2, y):
    return np.any(syms[y-1:y+2, x1-1:x2+2])

# for num in numbers (before called reshaped), 
#   we check if its a part, 
#   and if so, 
#       grab the original sequnce of numerals and convert to int
print(sum([int(''.join(array[y, x1:x2+1])) for [y, x1, x2] in numbers if checkPart(x1, x2, y)]))


# returns the indices of all * within the range of number
def checkGear(x1, x2, y):
    # make a mask of Trues around the number
    mask = np.zeros_like(numeric)
    mask[y-1:y+2, x1-1:x2+2] = True
    # if there is a gear within that mask we want it
    mask = np.logical_and(mask, gears)
    # return the indices of these valid gears
    return np.array(np.where(mask)).T

# creating a dictionary to store the gears in
g = {}

for [y, x1, x2] in numbers:
    valid = checkGear(x1, x2, y)
    # for each gear within range, we update its dictionary to store this number
    for [r, c] in valid:
        if (r, c) in g:
            g[(r, c)].append(int(''.join(array[y, x1:x2+1])))
        else:
            g[(r, c)] = [int(''.join(array[y, x1:x2+1]))]


# we just want the dictionarys with only 2 elements
print(sum([l[0] * l[1] for l in g.values() if len(l) == 2]))