#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Mr.yang
# Created Time : 2018/10/10 星期三 20:01:08
# File Name: cc.py
# Description:
# Editortool: vim8.0
"""
import requests
from bs4 import BeautifulSoup
headers = {
        'User-Agent': 
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
            }
id1 = "a84c8829e9904265872e2c0d2455ac02"
id2 = "1539172670613"
url = "http://www.nhfpc.gov.cn/xxgk/pages/viewdocument.jsp?manuscriptId=" + id1 + "&index=" + id2 
data = {
        "dispatchDate": "2015-06-24",
        "indexNum":	"000013610/2015-00239",
        "manuscriptId":	"a84c8829e9904265872e2c0d2455ac02",
        "publishedOrg":	"政务公开站点",
        "staticUrl":    "/zwgkzt/tgs/201506/a84c8829e9904265872e2c0d2455ac02.shtml",
        "topic":        "",
        "topictype":	"",
        "utitle":	"体改司",
        "wenhao":	"无"
        }
print(url)
r = requests.post(url, data=data, headers=headers)
print(r.status_code)
soup = BeautifulSoup(r.text, 'lxml')
print(soup)





