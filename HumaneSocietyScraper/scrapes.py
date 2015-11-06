from bs4 import BeautifulSoup
import os
import requests
import urllib
import unicodedata
import datetime 

def retrieveItem(url, fileNameOut):
	file = urllib.URLopener()
	file.retrieve(url, fileNameOut)
d = datetime.datetime.now()
folderName = str('{:04d}'.format(getattr(d, 'year')))+str('{:02d}'.format(getattr(d, 'month')))+str('{:02d}'.format(getattr(d, 'day')))+str('{:02d}'.format(getattr(d, 'hour')))+str('{:02d}'.format(getattr(d, 'minute')))+str('{:02d}'.format(getattr(d, 'second')))+str('{:06d}'.format(getattr(d, 'microsecond'))) 
url = "https://www.boulderhumane.org/animals/adoption/cats"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "html.parser")
links = []
animalNum = 0
if not os.path.isdir(folderName):
        os.makedirs(folderName)
	print folderName
for link in soup.find_all("div",{"class":"views-row"}):
	animalDatas=[]
	attrID=0
	
	for tastyData in link.find_all("div",{"class":"views-field"}):
		if attrID == 0:
			attr = tastyData.find("img")["src"]
			retrieveItem(attr, folderName+"/"+str(animalNum)+".jpg")
			animalDatas.append(str(attr))
			animalDatas.append(str(animalNum))
		elif attrID==2: #name
			attr = tastyData.find("a").getText()
			animalDatas.append(str(attr))
		elif attrID in [1,3,4]:
			attr = tastyData.find("div",{"class":"field-content"}).getText()
			animalDatas.append(str(attr))
		elif attrID == 5:
			try:
				attr = tastyData.find("font").getText()
			except AttributeError:
				attr = "None"
			animalDatas.append(str(attr))
		elif 6<=attrID<=8:
			attr = tastyData.find("span",{"class":"field-content"}).getText()
			animalDatas.append(str(attr))
		attrID = attrID + 1
	links.append(animalDatas)
	animalNum = animalNum + 1
file = open(folderName+"/results.txt", "w")
file.write("%s" % links)
file.close()
