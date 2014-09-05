import requests
import random
import urllib.request
from bs4 import BeautifulSoup
'''
def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://buckysroom.org/trade/search.php?page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('img'):
            href = "https://buckysroom.org" + link.get('img')
            title = link.string
            #print (title)
            #print (href)
            get_single_item_data(href)
        page += 1

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    #for item_name in soup.findAll('a', {'div': 'i-name'}):
        #print(item_name.string)
    for link in soup.findAll('img'):
           href = "https://buckysroom.org" + link.get('href')
        #print(href)



trade_spider(1)
'''
def downloadWebImage(url):
    name = random.randrange(1, 1000)
    fullName = str(name) + ".jpg"
    urllib.request.urlretrieve(url, url[20:])
    '''
    if url[len(url)-3]=="j" or url[len(url)-3]=="p":
        urllib.request.urlretrieve(url, fullName)
        print(url[len(url)-3])
        print(fullName)
    '''
def trade_spider(url):
    #url = 'http://boards.4chan.org/b/' #+ str(page)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll('a', {'class': 'fileThumb'}):
        #href = "http://boards.4chan.org/b/" + link.get('src')
        title = link.get('href')
        href = "http:"+title
        downloadWebImage(href)
        print (title)
inputURL=input("Enter the url for the 4chan page whose images you would like to grab: \n")
trade_spider(inputURL)