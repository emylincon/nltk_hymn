from nltk.tokenize import sent_tokenize
from nltk.corpus import wordnet

'''
s = open("C:/Users/emyli/PycharmProjects/nltk_song/hymns/amazing_grace", 'r').read()
tok = sent_tokenize(s)
t = s.split()
print(t[1])
'''

symn = wordnet.synsets('love')
li = []
#print(symn[2].lemmas()[0].name())

for i in symn:
    li.append(symn[i].lemmas()[0].name())
print(set(li))
