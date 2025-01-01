import numpy as np
import regex as re

data = np.array([[x for x in y] for y in open('input/d4').read().splitlines()])

getDiagonals = lambda mat : [mat.diagonal(offset) for offset in range(-mat.shape[0] + 1, mat.shape[1])]
search       = lambda mat, pattern : sum([len(re.findall(pattern, ''.join(x), overlapped=True)) for x in mat])

print(sum([search(x, r'SAMX|XMAS') for x in [data, data.T, getDiagonals(data), getDiagonals(np.fliplr(data))]]))

def searchAndReplace(mat, pattern = r'SAM|MAS'):
    newMat = []
    for x in mat:
        line = ''.join(x)
        newLine = np.zeros_like(x, dtype=np.int16)
        aS = [x.start(0) + 1 for x in re.finditer(pattern, line, overlapped=True)]
        newLine[aS] = 1
        newMat.append(newLine)
    return newMat

# https://github.com/numpy/numpy/issues/18000
def fillMat(oldMat, diag):
    mat = np.zeros_like(oldMat, dtype=np.int16)
    diag[:(len(diag) // 2)] = diag[:(len(diag) // 2)][::-1]
    for d, o in zip(diag, [offset for offset in range(-mat.shape[0] + 1, mat.shape[1])]):
        if o >= 0:
            np.fill_diagonal(mat[:, o:], d)
        else:
            np.fill_diagonal(mat[o:, :], d)            
    return mat

print(np.sum((fillMat(data, searchAndReplace(getDiagonals(data))) + np.fliplr(fillMat(data, searchAndReplace(getDiagonals(np.fliplr(data)))))) == 2))