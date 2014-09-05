import requests
import random
import urllib.request
from bs4 import BeautifulSoup

def trade_spider(url):
    print("Working...")
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll('a', {'class': 'fileThumb'}):
        href = "http:"+link.get('href')
        urllib.request.urlretrieve(href, href[20:])
inputURL=input("Enter the url for the 4chan page whose images you would like to grab: \n")
trade_spider(inputURL)
print("Done!")