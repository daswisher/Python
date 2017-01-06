#!/usr/bin/env python

import time

now = time.localtime()

if now.tm_isdst:
	print time.tzname[1]
else:
	print time.tzname[0]

print time.tzname

print time.strftime("%a, %d %b %Y %H:%M:%S %p", time.localtime())

print
print ("Epoch: January 1, 1970")
print ("Seconds since epoch: %i" % time.time())
