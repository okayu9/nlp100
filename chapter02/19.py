import fileinput


freqs = {}
for line in fileinput.input():
    string = line.rstrip().split('\t')[0]
    if string not in freqs:
        freqs[string] = 0
    freqs[string] += 1

sorted_freqs = sorted(freqs.items(), key=lambda x: x[1], reverse=True)

for string, freq in sorted_freqs:
    print(freq, string, sep='\t')
