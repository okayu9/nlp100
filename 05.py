from more_itertools import windowed


def ngram(n, seq):
    ngram_list = windowed(seq, n)
    return ngram_list


sentence = 'I am an NLPer'

words = sentence.split()
word2gram = ngram(2, words)
print(*word2gram)

char2gram = ngram(2, sentence)
print(*char2gram)
