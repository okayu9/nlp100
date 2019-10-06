import random


def typoglycemia_word(word):
    if len(word) <= 4:
        return word
    top = word[0]
    mdl = word[1:-1]
    btm = word[-1]
    shuffled_mdl = ''.join(random.sample(mdl, len(mdl)))
    return top + shuffled_mdl + btm


def typoglycemia(sent):
    words = sent.split(' ')
    typoglycemia_words = map(typoglycemia_word, words)
    return ' '.join(typoglycemia_words)


sentence = ("I couldn't believe that I could actually understand "
            "what I was reading : the phenomenal power of the human mind .")
ans = typoglycemia(sentence)
print(ans)
