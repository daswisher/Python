from bs4 import BeautifulSoup
import requests

url = "https://www.boulderhumane.org/animals/adoption/cats"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data)
links = []
for link in soup.find_all("div",{"class":"views-row"}):
	animalDatas=[]
	attrID=0
	for tastyData in link.find_all("div",{"class":"views-field"}):
		if attrID == 0:
			attr = tastyData.find("img")["src"]
			animalDatas.append(attr)
		elif attrID==2:
			attr = tastyData.find("a")
			#attr = attr[attr.index('>'):attr.index('<')]
			#attr = attr[attr.find('<',2):attr.find('>',2)]
			print attr
		elif attrID in [1,3,4]:
			attr = tastyData.find("div",{"class":"field-content"})
			#print attr
		elif attrID == 5:
			attr = tastyData.find("font")
			#print attr
		elif 6<=attrID<=8:
			attr = tastyData.find("span",{"class":"field-content"})
			#print attr
		attrID = attrID + 1
	links.append(animalDatas)
#print links
