from nltk.corpus import wordnet
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

ps = PorterStemmer()

stop_words = set(stopwords.words("english"))


def read_file():
    s = open("C:/Users/emyli/PycharmProjects/nltk_song/hymns/amazing_grace", 'r').read()
    return s


def remove_stopwords():
    enter_words = read_file()
    words = word_tokenize(enter_words)
    #stemmed = [ps.stem(w) for w in words]
    filt_sen = [w for w in words if not w in stop_words]
    good = [w for w in filt_sen if len(w)>2]
    better = [i for i in [w.lower() for w in good] if i!='the' and i!='and']
    return better


def find_symn(word):
    symn = wordnet.synsets(word)
    li = []
    #print(symn[2].lemmas()[0].name())

    for i in range(len(symn)):
        li.append(symn[i].lemmas()[0].name())
    return set(li)


def word_similarity(word1, word2):
    w1 = wordnet.synset("{}.v.01".format(word1))
    w2 = wordnet.synset("{}.v.01".format(word2))
    return w1.wup_similarity(w2)


def word_freq(words):
    words = nltk.FreqDist(words)
    print(words.keys())
    print(words.most_common(15))
    print(words.max())
    words.plot(15)


# find_symn('love')
# print(word_similarity('love', 'like'))
# word_freq(remove_stopwords())
# print(remove_stopwords())

def hymn():
    sym = find_symn('love')
    hymn = nltk.FreqDist(remove_stopwords())
    sym = [w.split('_') for w in sym]
    '''
    for i in sym:
        if i in hymn.keys():
            print("{}: {}".format(i, hymn[i]))
        else:
            print('no match for ', i)
    h = hymn['love']
    print(h)
    hymn.plot(10)
    '''
    dic = []
    for i in sym:
        lent = 0
        for j in i:
            if j in hymn.keys():
                lent += 1
            if lent == len(i):
                dic.append(' '.join(i))
    print(dic)


hymn()
