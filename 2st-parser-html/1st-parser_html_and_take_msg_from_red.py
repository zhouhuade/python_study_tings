from urllib.request import urlopen 
from urllib.error import HTTPError 
from bs4 import BeautifulSoup
def getHtml(url):
     try:
         html = urlopen(url) 
     except HTTPError as e:
         return None 
     try:
         bsObj = BeautifulSoup(html.read(),"html.parser")
     except AttributeError as e:
         return None 
     return bsObj
msg = getHtml("http://www.pythonscraping.com/pages/warandpeace.html")
if msg == None:
    print("Title could not be found") 
else:
#    print(msg)
    nameList = msg.findAll("span", {"class":"green"}) 
    for name in nameList:
        print(name.get_text())
