sentence = ('Hi He Lied Because Boron Could Not Oxidize Fluorine. '
            'New Nations Might Also Sign Peace Security Clause. '
            'Arthur King Can.')
index_1char = set((1, 5, 6, 7, 8, 9, 15, 16, 19))

words = sentence.split()

elm_dic = {}
for i, word in enumerate(words):
    elm = word[0] if i+1 in index_1char else word[:2]
    elm_dic[elm] = i+1

print(elm_dic)
