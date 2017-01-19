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
msg = getHtml("https://en.wikipedia.org/wiki/Main_Page")
if msg == None:
    print("Title could not be found") 
else:
    for link in msg.find("div", {"id":"bodyContent"}).findAll("a",
            href=re.compile("^(/wiki/)((?!:).)*$")): 
#        if 'href' in link.attrs:
            print(link.attrs['href'])
