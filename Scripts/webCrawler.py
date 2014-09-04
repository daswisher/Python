import requests
import random
from bs4 import BeautifulSoup
import urllib.request

def spider(max_pages, IURL):
	page = 1
	while page <= max_pages:
		url = IURL #+ str(page)
		src = requests.get(url)
		txt = src.text
		soup = BeautifulSoup(txt) 
		for link in soup.findAll('img'): #This pulls all of the images
			#findAll('a', {'class': 'class-name'}) would get all links with the class of class-name
			href = link.get('img')
			name = random.randrange(1, 1000)
			fullName = str(name) + ".jpg"
			urllib.request.urlretrieve(href, fullName)
		page += 1
spider(1, "http://boards.4chan.org/g/")
