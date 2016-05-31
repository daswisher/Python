from __future__ import division

import nltk
from nltk.corpus import PlaintextCorpusReader

#rootOfCorpus = "~/GitHub/Python/Reference/nltk"
rootOfCorpus = ""
#newCorpus = PlaintextCorpusReader(rootOfCorpus,'.*')
newCorpus = PlaintextCorpusReader(rootOfCorpus,'.*')
print(type(newCorpus))
print newCorpus.fileids()
print newCorpus.abspaths()

rawText = newCorpus.raw()
print len(rawText)

tokens = nltk.word_tokenize(rawText)

print len(tokens)

textSimpson = nltk.Text(tokens)

print type(textSimpson)

vocabularyused = set(textSimpson)

print len(vocabularyUsed)

print sorted(set(textSimpson))

myWord = "KILL"

textSimpson.count(myword)

print textSimpson.collocations()

print textSimpson.concordance(myWord)

myWord = "GLOVE"

print textSimpson.concordance(myWord)

myWord = "intent"

print textSimpson.similar(myWord)

simpsonVocab = textSimpson.vocab()

type(simpsonVocab)

simpsonVocab.items()
