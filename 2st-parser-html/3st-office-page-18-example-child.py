from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,"html.parser")
for child in bsObj.find("tr",{"id":"gift4"}).children:
    print(child)
