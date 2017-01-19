from urllib.request import urlopen 
from urllib.error import HTTPError 
from bs4 import BeautifulSoup
import re

def getHtml(url):
     try:
         html = urlopen(url) 
     except HTTPError as e:
         return None 
     try:
         bsObj = BeautifulSoup(html,"html.parser")
     except AttributeError as e:
         return None 
     return bsObj

def getLinks(articleUrl):
    html = getHtml("http://en.wikipedia.org"+articleUrl)
    return html.find("div", {"id":"bodyContent"}).findAll("a",
                href=re.compile("^(/wiki/)((?!:).)*$"))
#linkList = getLinks("/wiki/Kevin_Bacon")
for link in getLinks("/wiki/Kevin_Bacon"):
    print(link.attrs['href'])
