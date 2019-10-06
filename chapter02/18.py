import fileinput


lines = [line.rstrip().split('\t') for line in fileinput.input()]
sorted_lines = sorted(lines, key=lambda x: int(x[2]), reverse=True)

for line in sorted_lines:
    print(*line, sep='\t')
