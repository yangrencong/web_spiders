#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Mr.yang
# Created Time : 2018/9/22 星期六 13:16:49
# File Name: mydb.py
# Description:
"""
import requests
from bs4 import BeautifulSoup
import MySQLdb

conn = MySQLdb.connect(
        host = 'localhost',
        user = 'root',
        passwd = '1452581359',
        db = 'scraping',
        charset = 'utf8'
        )
cur = conn.cursor()

link = "http://www.santostang.com/"
headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"
        }

r = requests.get(link ,headers = headers) 

soup = BeautifulSoup(r.text ,"lxml")
title_list = soup.find_all("h1" ,class_ = "post-title")
for eachone in title_list:
    url = eachone.a['href']
    title = eachone.a.text.strip()
    cur.execute("insert into urls (url ,content) values (%s ,%s)" ,(url[:10] ,title))

cur.close()
conn.commit()
conn.close()


