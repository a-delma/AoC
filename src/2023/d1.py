import re

data = open('d1.in').read().splitlines()
lines = [re.findall('(\d)', l) for l in data]
digits = [int(l[0] + l[-1]) for l in lines]
print(sum(digits))


lines = data
numerals = ['\t', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
for idx, i in enumerate(numerals):
    lines = [l.replace(i, f'{i}_{idx}_{i}') for l in lines]
lines = [re.findall('(\d)', l) for l in lines]
digits = [int(l[0] + l[-1]) for l in lines]

print(sum(digits))