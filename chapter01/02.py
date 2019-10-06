# coding: utf-8
from itertools import chain

s1 = 'パトカー'
s2 = 'タクシー'
ans = ''.join(chain(*zip(s1, s2)))
print(ans)
