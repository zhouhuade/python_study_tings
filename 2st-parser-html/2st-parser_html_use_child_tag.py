from urllib.request import urlopen 
from urllib.error import HTTPError 
from bs4 import BeautifulSoup
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
msg = getHtml("http://www.pythonscraping.com/pages/page3.html")
if msg == None:
    print("Title could not be found") 
else:
#    print(msg)
    for child in msg.find("table",{"id":"giftList"}).children:
        print(child)
