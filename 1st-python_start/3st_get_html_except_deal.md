>我们看看爬虫 import 语句后面的第一行代码,如何处理那里可能出现的异常: 
`html = urlopen("http://www.pythonscraping.com/pages/page1.html")`
这行代码主要可能会发生两种异常:
- 网页在服务器上不存在(或者获取页面的时候出现错误)
- 服务器不存在

>第一种异常发生时,程序会返回 HTTP 错误。HTTP 错误可能是“404 Page Not Found”“500 Internal Server Error”等。所有类似情形,urlopen 函数都会抛出“HTTPError”异常。我们 可以用下面的方式处理这种异常:
``` 
try:
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
except HTTPError as e: 
    print(e)
    # 返回空值,中断程序,或者执行另一个方案 
else:
    # 程序继续。注意:如果你已经在上面异常捕捉那一段代码里返回或中断(break), # 那么就不需要使用else语句了,这段代码也不会执行
    #如果程序返回 HTTP 错误代码,程序就会显示错误内容,不再执行 else 语句后面的代码。
```    
>如果服务器不存在(就是说链接 http://www.pythonscraping.com/ 打不开,或者是 URL 链接 写错了),urlopen 会返回一个 None 对象。这个对象与其他编程语言中的 null 类似。我们 可以增加一个判断语句检测返回的 html 是不是 None:
```    
    if html is None:
       print("URL is not found")
    else:
# 程序继续
```    
    当然,即使网页已经从服务器成功获取,如果网页上的内容并非完全是我们期望的那样, 仍然可能会出现异常。每当你调用 BeautifulSoup 对象里的一个标签时,增加一个检查条件 保证标签确实存在是很聪明的做法。
