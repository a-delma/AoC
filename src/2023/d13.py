import numpy as np

sets = [np.array([[0 if c == '.' else 1 for c in l ] for l in s]) for s in [l.splitlines() for l in open('d13.in').read().split('\n\n')]]

def findSplit(s, cond):
    for arr, mult in zip([s, s.T], [100, 1]):
        for i in range(1, arr.shape[0]):
            top, bottom = arr[:i], arr[i:]
            size = min(top.shape[0], bottom.shape[0])
            top, bottom = top[-size:], np.flip(bottom[:size], axis=0)
            if cond(top, bottom):
                return i * mult
    print("QwQ")

print(sum([findSplit(s, lambda x, y: np.array_equal(x, y)) for s in sets]), 
      sum([findSplit(s, lambda x, y: np.sum(np.abs(x - y)) == 1) for s in sets]))
