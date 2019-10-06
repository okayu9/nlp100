import fileinput


for line in fileinput.input():
    line = line.rstrip()
    replaced_line = line.replace('\t', ' ')
    print(replaced_line)
