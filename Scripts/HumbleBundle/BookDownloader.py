'''
Usage:
1. Go to the page that has all of the Humble Bundle book links
2. Right click on the page and choose inspect element
3. Open the console tab and paste the following javascript block into the console
==========================================================================
var allLinks = {};
$('a').each(function(x){ 
	var obj = $(this)[0]; 
	if(['PDF', 'MOBI', 'EPUB', 'XPS', 'DOC', 'PRC'].includes(obj['innerText'])){
		try{
			var previousTitle = obj.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.children[1].children[0].children[0];
			var fileName = previousTitle.innerHTML.replace(/[^\x00-\x7F]/g, "").trim().replace(/\s+/g,'-') + "." + obj['innerText'].toLowerCase();
			var md5sum = obj.parentElement.parentElement.children[1].children[0].children[1];
			md5sum.click();
			md5sumValue = md5sum.innerText.replace(/\s/gm, '');
			allLinks[fileName] = [obj['href'], md5sumValue];
		}
		catch(err){}
	}
});

console.log(JSON.stringify(allLinks));
==========================================================================
4. Copy and paste the javascript output onto the line that assigns the variable "allLinks" (line 43)
5. Run the python script
6. ????
7. Profit.
'''




import urllib
import urllib2
import hashlib
import multiprocessing
from multiprocessing.dummy import Pool as ThreadPool 

allLinks = '' # Copy and paste the output from the javascript between the quotes

def getThatBook(stuff):
	print "Getting %s" % stuff[0]
	try:
		response = urllib2.urlopen(stuff[1][0])
		urllib.URLopener().retrieve(response.geturl(), stuff[0])

		expectedHash = stuff[1][1]

		data = open(stuff[0], 'rb').read()
		md5Returned = hashlib.md5(data).hexdigest()

		if expectedHash != md5Returned:
			print
			print
			print "Failure:", stuff[0], expectedHash, md5Returned
			print
			print
		else:
			print "Success:", stuff[0]
		

	except Exception as e:
		print "Failed to get %s" % stuff[0]
		print e

parsedStuff = []
for link in allLinks:
	parsedStuff.append([link, allLinks[link]])

pool = ThreadPool(multiprocessing.cpu_count())

pool.map(getThatBook, parsedStuff)

pool.close()
pool.join()

