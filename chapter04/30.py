from more_itertools import split_at


def sent2dics(sent):
    return list(map(morph2dic, sent))


def morph2dic(morph):
    surface, detail = morph.split('\t')
    detail = detail.split(',')
    pos = detail[0]
    pos1 = detail[1]
    base = detail[6] if len(detail) == 9 else ''
    return {
        'surface': surface,
        'pos': pos,
        'pos1': pos1,
        'base': base
    }


text_mecab_filename = 'neko.txt.mecab'

with open(text_mecab_filename, 'r') as f:
    text_mecab = [line.rstrip() for line in f]
sents_mecab = split_at(text_mecab, lambda x: x == 'EOS')
sents_mecab = map(sent2dics, sents_mecab)

sents_mecab = list(sents_mecab)
print(*sents_mecab[:5], sep='\n')
