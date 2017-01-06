from bs4 import BeautifulSoup
import requests
import urllib

url = "http://www.nytimes.com" #Can be any publicly accessible website (i.e. doesn't require a login)
r = requests.get(url) # makes an http request. Printing will print the http request status code
data = r.text # converts the data from the http request to be plaintext
soup = BeautifulSoup(data, "html.parser") #Flags bs4 to parse the plaintext data as an html document

'''
Parameter for findAll is whatever html tag you want to pick apart
A second parameter can be added to refine the search based upon class or id of the html tag
	Ex soup.findAll('div', {'class': 'article-body'})
'''
for tag in soup.findAll('img'):
	#do stuff
	print tag #Place holder
	
	'''
	In order to integrate something such as image scraping, it's necessary to
	include urllib in the code. To make this work, uncomment the comment block
	block below as well as the import urllib at the top of the code.

	NOTE: It is not necessary to use error handling (the try/except lines) to 
	run this code. I added it in case a website has a file with a bad name.
	'''
	
	'''
	imgUrl = tag.get('src') #Extracts the url from the html tag that was found
	imgName = imgUrl[imgUrl.rfind('/')+1:] #Extracts the file name from the end of the url
	#urllib.URLopener().retrieve(imgUrl, imgName) #Downloads a file from the specified url and saves it to the specified name
	try:
		urllib.URLopener().retrieve(imgUrl, imgName)
	except (IOError):
		pass
	'''	
