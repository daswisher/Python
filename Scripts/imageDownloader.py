import random
import urllib.request

def downloadWebImage(url):
	name = random.randrange(1, 1000)
	fullName = str(name) + ".jpg"
	urllib.request.urlretrieve(url, fullName)

#downloadWebImage("google.com/image.jpg")
