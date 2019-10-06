import sys
from more_itertools import divide


n = int(sys.argv[1])
input_filename = sys.argv[2]
output_filename = sys.argv[3]

with open(input_filename, 'r') as fin:
    for i, chunk in enumerate(divide(n, fin)):
        with open(f'{output_filename}.{i}', 'w') as fout:
            for line in chunk:
                print(line, end='', file=fout)
