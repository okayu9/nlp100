import re

sentence = ('Now I need a drink, alcoholic of course, '
            'after the heavy lectures involving quantum mechanics.')
sentence_no_punc = re.sub(r'[,.]', '', sentence)
words = sentence_no_punc.split()
words_len = map(len, words)
print(*words_len)
