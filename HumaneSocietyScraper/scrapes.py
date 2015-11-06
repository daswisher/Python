from bs4 import BeautifulSoup
import requests
import urllib
import unicodedata

def stripTag(element):
	return BeautifulSoup(element, "lxml").getText()

def retrieveItem(url, fileNameOut):
	file = urllib.URLopener()
	file.retrieve(url, fileNameOut)
url = "https://www.boulderhumane.org/animals/adoption/cats"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "html.parser")
links = []
animalNum = 0
for link in soup.find_all("div",{"class":"views-row"}):
	animalDatas=[]
	attrID=0
	
	for tastyData in link.find_all("div",{"class":"views-field"}):
		if attrID == 0:
			attr = tastyData.find("img")["src"]
			#animalDatas.append(attr)
			retrieveItem(attr, str(animalNum)+".jpg")
			animalDatas.append(attr)
		elif attrID==2: #name
			attr = tastyData.find("a").getText()
			#attr = attr[attr.index('>'):attr.index('<')]
			#attr = attr[attr.find('<',2):attr.find('>',2)]
			#print attr
			animalDatas.append(attr)
		elif attrID in [1,3,4]:
			attr = tastyData.find("div",{"class":"field-content"}).getText()
			#print attr
			animalDatas.append(attr)
		elif attrID == 5:
			try:
				attr = tastyData.find("font").getText()
			except AttributeError:
				attr = "None"
			#print attr
			animalDatas.append(attr)
		elif 6<=attrID<=8:
			attr = tastyData.find("span",{"class":"field-content"}).getText()
			#print attr
			animalDatas.append(attr)
		attrID = attrID + 1
	for val in animalDatas:

	links.append(animalDatas)
	animalNum = animalNum + 1
print links
