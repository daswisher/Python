#!/usr/bin/env python

import nltk

from urllib import urlopen

url = "http://www.gutenberg.org/files/2760/2760.txt"

raw = urlopen(url).read()

type(raw)

len(raw)

tokenList = nltk.word_tokenize(raw)

type(tokenList)

len(tokenList)

