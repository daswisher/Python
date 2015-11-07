from bs4 import BeautifulSoup
import requests
import urllib

url = "" 
r = requests.get(url) 
data = r.text 
soup = BeautifulSoup(data, "html.parser") 

for tag in soup.findAll(''):
	print tag 
	'''
	imgUrl = tag.get('src') 
	imgName = imgUrl[imgUrl.rfind('/')+1:] 
	#urllib.URLopener().retrieve(imgUrl, imgName) 
	try:
		urllib.URLopener().retrieve(imgUrl, imgName)
	except (IOError):
		pass
	'''	
