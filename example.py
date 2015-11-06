from bs4 import BeautifulSoup
import requests

url = "http://www.nytimes.com"
r = requests.get(url)
data = r.text #gets data from request (not printable in windows yet) probs unicode
soup = BeautifulSoup(data, "html.parser") #printable now. probs ascii now
for link in soup.find_all("div",{"class":"b-column"}):
	for masLinks in link.find_all("img"):
		print masLinks
