#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Mr.yang
# Created Time : 2018/9/16 星期日 20:12:52
# File Name: bsoup.py
# Description:
"""
import requests
from bs4 import BeautifulSoup

link = "http://www.santostang.com/"
headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
        'Host':
        'www.santostang.com'
        }

r = requests.get(link ,headers = headers)

soup = BeautifulSoup(r.text ,"html.parser")

first_title = soup.find("h1" ,class_ = "post-title").a.text.strip()
print("第1篇文章的标题是：" ,first_title)

title_list = soup.find_all("h1" ,class_ = "post-title")

for i in range(len(title_list)):
    title = title_list[i].a.text.strip()
    print('第%s篇文章的标题是: %s' %(i+1 ,title))

