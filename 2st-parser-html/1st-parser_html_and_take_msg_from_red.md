# 什么时候使用 get_text() 与什么时候应该保留标签?
.get_text() 会把你正在处理的 HTML 文档中所有的标签都清除,然后返回 一个只包含文字的字符串。假如你正在处理一个包含许多超链接、段落和标 签的大段源代码,那么 .get_text() 会把这些超链接、段落和标签都清除掉, 只剩下一串不带标签的文字。
用 BeautifulSoup 对象查找你想要的信息,比直接在 HTML 文本里查找信 息要简单得多。通常在你准备打印、存储和操作数据时,应该最后才使 用 .get_text()。一般情况下,你应该尽可能地保留 HTML 文档的标签结构。

#BeautifulSoup的find()和findAll()
BeautifulSoup 里的 find() 和 findAll() 可能是你最常用的两个函数。借助它们,你可以通
过标签的不同属性轻松地过滤 HTML 页面,查找需要的标签组或单个标签。
这两个函数非常相似,BeautifulSoup 文档里两者的定义就是这样: 
>findAll(tag, attributes, recursive, text, limit, keywords)
>find(tag, attributes, recursive, text, keywords)
    很可能你会发现,自己在 95% 的时间里都只需要使用前两个参数:tag 和 attributes。但
    是,我们还是应该仔细地观察所有的参数。
    
前面的使用例子：`bsObj.findAll("span", {"class":"green"})`
    
