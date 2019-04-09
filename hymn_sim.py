from nltk.corpus import wordnet
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import matplotlib.pyplot as plt
from threading import Thread
from drawnow import *

ps = PorterStemmer()

stop_words = set(stopwords.words("english"))


def read_file(hymn):
    global loaded_hymn
    loaded_hymn = open("C:/Users/emyli/PycharmProjects/nltk_song/hymns/{}.txt".format(hymn), 'r').read()
    return loaded_hymn


def remove_stopwords():
    enter_words = loaded_hymn
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

    dic = []
    for i in sym:
        lent = 0
        for j in i:
            if j in hymn.keys():
                lent += 1
            if lent == len(i):
                dic.append(' '.join(i))
    for i in dic:
        print('{} : {}'.format(i, hymn[i]))
    freq = 0
    for i in dic:
        freq+=hymn[i]
    print('Total similarity words : {}'.format(freq))
    syst = [' '.join(i) for i in sym]
    _plot = {i:0 for i in syst}
    if i in dic:
        _plot[i] = hymn[i]

    return [hymn, _plot]


def plot(dic):

    fig1 = plt.figure('figure 1')
    po = list(range(1, len(dic)+1))
    namey = dic.keys()
    chart = dic.values()
    fig1 = plt.xticks(po, namey)
    fig1= plt.bar(po, chart)


def plot_hymn(var):

    fig2 = plt.figure('figure 2')
    fig2 = var.plot(10)


def the_thread():
    x = hymn()
    var = x[0]
    dic = x[1]
    h2 = Thread(target=plot(dic))
    h2.start()
    h1 = Thread(target=plot_hymn(var))

    h1.start()


def ppt():
    drawnow(the_thread)


def main():
    try:
        read_file(input('Enter hymn: ').strip())
        ppt()
        # the_thread()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
