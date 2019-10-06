import fileinput


col1_filename = 'col1.txt'
col2_filename = 'col2.txt'

with open(col1_filename, 'w') as c1, open(col2_filename, 'w') as c2:
    for line in fileinput.input():
        line = line.rstrip()
        cols = line.split('\t')
        col1 = cols[0]
        col2 = cols[1] if 2 <= len(cols) else ''
        print(col1, file=c1)
        print(col2, file=c2)
