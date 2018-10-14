#！DT
#coding: UTF-8
#爬虫须遵守ROBOTS协议
import requests
from bs4 import BeautifulSoup
#从bs4库中导入Beatifulsoup
link = "http://www.santostang.com/"
#伪装浏览器进行访问

headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'} 
r= requests.get(link ,headers = headers)

#使用这段代码来解析这个网页代码
soup = BeautifulSoup(r.text ,'html.parser')
title = soup.find("h1" ,class_ = "post-title").a.text.strip()
print(title)
with open('title.txt' ,"a+") as f:
    f.write(title)
    f.close()
