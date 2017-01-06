from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

display = Display(visible=0, size=(1,1))
display.start()

url = "http://goodfuckingdesignadvice.com/#/advice/"
adviceNumber = 11

browser = webdriver.Firefox()
browser.get(url+str(adviceNumber))
htmlSource = browser.page_source

soup = BeautifulSoup(htmlSource, 'html.parser')
advice = soup.findAll('h1', {'id':'advice-txt'})
print str(adviceNumber)+": "+advice[0].getText()
browser.quit()
display.stop()
