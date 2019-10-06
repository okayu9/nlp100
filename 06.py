from more_itertools import windowed


def ngram(n, seq):
    ngram_list = windowed(seq, n)
    return ngram_list


word1 = 'paraparaparadise'
word2 = 'paragraph'
word1_char2gram = set(ngram(2, word1))
word2_char2gram = set(ngram(2, word2))

union = word1_char2gram | word2_char2gram
diff = word1_char2gram - word2_char2gram
intersection = word1_char2gram & word2_char2gram

print('union:', union)
print('diff:', diff)
print('intersection:', intersection)
