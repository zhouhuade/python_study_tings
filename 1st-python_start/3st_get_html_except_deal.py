from urllib.request import urlopen
from bs4 import BeautifulSoup
try:
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
except HTTPError as e:  
    print(e)
            # 返回空值,中断程序,或者执行另一个方案  
else:
    if html is None:
        print("URL is not found")
    else:
        bsObj = BeautifulSoup(html.read(),"html.parser")
        print(bsObj.body)

