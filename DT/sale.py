#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Mr.yang
# Created Time : 2018/9/18 星期二 15:45:54
# File Name: sale.py
# Description:
"""
import requests
from bs4 import BeautifulSoup

headers = {
        'user-agent': 
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
        }
#此处页数为想要爬取数据的页数
for i in range(1 ,11):
    link = "https://beijing.anjuke.com/sale/p" + str(i)
    r = requests.get(link ,headers = headers)

    soup = BeautifulSoup(r.text ,'lxml')
    house_list = soup.find_all('li' ,class_ = "list-item")
    print("你将要爬取%s页"  %(i))
    for house in house_list:
        name = house.find("div" ,class_ = 'house-title').a.text.strip()
        price = house.find("span" ,class_ = 'price-det').text.strip()
        price_area = house.find("span" ,class_ = 'unit-price').text.strip()
        #find函数寻找标签内容第一次出现的地方
        no_room = house.find("div" ,class_ = 'details-item').span.text
        
        area = house.find("div" ,class_ = 'details-item').contents[3].text
        floor = house.find("div" ,class_ = 'details-item').contents[5].text
        year = house.find("div" ,class_ = 'details-item').contents[7].text
        broker = house.find("span" ,class_ = 'brokername').text
        broker = broker[1:]
        address = house.find('span' ,class_ = 'comm-address').text.strip()
        address = address.replace('\xa0\xa0\n                   ',' ')
        tag_list = house.find_all('span' ,class_='item-tags')
        tags = [i.text for i in tag_list]
        print(name ,price ,price_area ,no_room ,area ,floor ,year ,broker ,address ,tags)



