import fileinput
from itertools import islice


for line in islice(fileinput.input(), 10):
    print(line, end='')
