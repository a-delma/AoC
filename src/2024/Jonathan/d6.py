from aoc_utils import *
import numpy as np
from collections import Counter
import sys
sys.setrecursionlimit(100000)
#

LEFT = (0,-1)
RIGHT = (0,1)
UP = (-1, 0)
DOWN = (1, 0)
DIRS = [UP, RIGHT, DOWN, LEFT]

### Part 1: Simulate walking, and record number of positions seen
def take_step(arr, curr_row, curr_col, dir_index):
    dir = DIRS[dir_index]
    new_r, new_c = curr_row + dir[0], curr_col + dir[1]
    if not in_bound(new_r, new_c, arr):
        return Counter([str(x) for x in np.nditer(arr)])["X"]
    elif arr[new_r, new_c] == "#":
        dir_index = (dir_index + 1) % len(DIRS)
        return take_step(arr, curr_row, curr_col, dir_index)
    else:
        arr[new_r, new_c] = "X"
        return take_step(arr, new_r, new_c, dir_index)

### Part 2: Detect if there is a loop
def detect_loop(arr, curr_row, curr_col, dir_index, seen_before):
    # `seen_before` is set of (row, col, dir_index)
    if (curr_row, curr_col, dir_index) in seen_before:
        return True
    seen_before.add((curr_row, curr_col, dir_index))
    
    dir = DIRS[dir_index]
    new_r, new_c = curr_row + dir[0], curr_col + dir[1]
    if not in_bound(new_r, new_c, arr):
        return False
    elif arr[new_r, new_c] == "#":
        dir_index = (dir_index + 1) % len(DIRS)
        return detect_loop(arr, curr_row, curr_col, dir_index, seen_before)
    else:
        return detect_loop(arr, new_r, new_c, dir_index, seen_before)


def main(filename):
    with open(filename) as file:
        arr = np.array([list(l) for l in file.read().splitlines()], dtype=str)
        start_r, start_c = np.argwhere(arr == "^")[0]
        start_dir_index = 0
        arr[start_r, start_c] = "X"

        ### Part 1
        part1_num_seen = take_step(arr, start_r, start_c, start_dir_index)
        print("Part 1:", part1_num_seen)

        ### Part 2
        count = 0
        for row in range(len(arr)):
            print("Row ", row, "of", len(arr))
            for col in range(len(arr[0])):
                # the `and arr[row, col]=="X"` optimization is from Teo,
                #    and it reduces runtime from >3 min to ~40 seconds
                if ((row, col) != (start_r, start_c)) and arr[row, col]=="X":
                    arr_copy = np.copy(arr)
                    arr_copy[row, col] = "#"
                    count += detect_loop(arr_copy, start_r, start_c, start_dir_index, set())
        print("Part 2:", count)

if __name__ == "__main__":
    # filename = "../input/temp"
    filename = "input/d6"
    print(filename)
    main(filename)