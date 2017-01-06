#!/usr/bin/env python

def fooFunc():
	print "Goodbye"

def barFunc():
	print "world"


dispatcher = {
	"foo": fooFunc,
	"bar": barFunc
}
dispatcher["foo"]()
dispatcher["bar"]()
