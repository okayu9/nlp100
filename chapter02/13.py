col1_filename = 'col1.txt'
col2_filename = 'col2.txt'

with open(col1_filename, 'r') as c1, open(col2_filename, 'r') as c2:
    for col1, col2 in zip(c1, c2):
        col1 = col1.rstrip()
        col2 = col2.rstrip()
        print(col1, col2, sep='\t')
