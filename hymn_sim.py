from nltk.tokenize import sent_tokenize
from nltk.corpus import wordnet

s = open("C:/Users/emyli/PycharmProjects/nltk_song/hymns/amazing_grace", 'r').read()
tok = sent_tokenize(s)
t = s.split()
print(t[1])
