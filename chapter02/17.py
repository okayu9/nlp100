import fileinput


uniq_string = set()
for line in fileinput.input():
    line = line.rstrip()
    string = line.split('\t')[0]
    if string not in uniq_string:
        print(string)
        uniq_string.add(string)
