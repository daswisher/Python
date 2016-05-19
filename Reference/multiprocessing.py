'''
from multiprocessing.dummy import Pool as ThreadPool 
pool = ThreadPool(4) 
results = pool.map(my_function, my_array)

#######Is equivalent


for item in my_array:
    results += my_function(item)
'''

import urllib2 
from multiprocessing.dummy import Pool as ThreadPool 

urls = [
  'http://www.python.org', 
  'http://www.python.org/about/',
  'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
  'http://www.python.org/doc/',
  'http://www.python.org/download/',
  'http://www.python.org/getit/',
  'http://www.python.org/community/',
  'https://wiki.python.org/moin/',
  ]

# Make the Pool of workers
pool = ThreadPool(4) 

# Open the urls in their own threads
# and return the results
results = pool.map(urllib2.urlopen, urls)

#close the pool and wait for the work to finish 
pool.close() 
pool.join() 

'''
Single thread:   14.4 seconds
       4 Pool:   3.1 seconds
       8 Pool:   1.4 seconds
      13 Pool:   1.3 seconds


Referenced:
http://stackoverflow.com/questions/2846653/how-to-use-threading-in-python
'''
