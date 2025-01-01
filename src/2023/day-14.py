from aoc_utils import *
import numpy as np
from collections import Counter
import functools
import itertools

FIXED = "#"
MOVING = "O"
EMPTY = "."

##############
### Part 1 ###
##############

def tilt(arr):
    new_arr = arr.copy()
    for j, col in enumerate(arr.T):
        chunks = "".join(col).split(FIXED)
        for i, chunk in enumerate(chunks.copy()):
            new_chunk = MOVING * (chunk.count(MOVING)) + EMPTY * (chunk.count(EMPTY))
            chunks[i] = new_chunk
        new_col_str = "#".join(chunks)
        new_col = np.array([c for c in new_col_str])
        new_arr[:,j] = new_col
    return new_arr

def count(arr):
    total = 0
    for r in range(len(arr)):
        row = arr[r]
        num_stones = "".join(row).count(MOVING)
        total += (len(arr) - r) * num_stones
    return total

##############
### Part 2 ###
##############

def cycle(arr):
    after_north = tilt(arr)
    after_west = tilt(np.rot90(after_north, 3))
    after_south = tilt(np.rot90(after_west, 3))
    after_east = tilt(np.rot90(after_south, 3))
    return np.rot90(after_east, 3)

def arr2str(arr):
    return " ".join(["".join(row) for row in arr])

def str2arr(s):
    return np.array([[c for c in row] for row in s.split(" ")])

def find_loop(arr):
    ERA = 1000000000
    timestamps = dict()
    for i in range(ERA):
        arr = cycle(arr)
        s = arr2str(arr)
        if s in timestamps:
            break
        else:
            timestamps[s] = i
    initial_time = timestamps[s]
    repeated_time = i
    print("REPEATED", i)
    period = repeated_time - initial_time
    print("PERIOD", period)
    num_reps = ((ERA - initial_time)//period)
    start_time = num_reps * period + initial_time
    arr = str2arr(s)
    for i in range(start_time, ERA - 1): # Why -1? Because it didn't work without it...
        arr = cycle(arr)
    print(count(arr))

############
### Main ###
############

def main(filename):
    with open(filename) as file:
        array = np.array([[c for c in s] for s in file.read().split("\n")])
        print(count(cycle(array))) # Part 1
        find_loop(array) # Part 2
        
if __name__ == "__main__":
    filename = "Input/test.txt"
    # filename = "Input/day-14.txt"
    main(filename)