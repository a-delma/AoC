import re

data = open('input/d3').read()
extract = lambda x : sum([int(a) * int(b) for a, b in re.findall(r'mul\((\d+),(\d+)\)', x)])
print(extract(data))
print(sum([extract(segment[segment.find("do()"):]) for segment in ('do()' + data).split("don't()") if segment.find("do()") != -1]))