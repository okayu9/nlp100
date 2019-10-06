import fileinput
from more_itertools import islice_extended


for line in islice_extended(fileinput.input(), -10, None):
    print(line, end='')
