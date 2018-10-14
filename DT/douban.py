#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Mr.yang
# Created Time : 2018/9/11 星期二 21:43:13
# File Name: douban.py
# Description: 一个关于豆瓣电影榜单250的简单爬虫
"""
import requests
from bs4 import BeautifulSoup
def get_movies():

    headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/68.0.3440.84 Safari/537.36',
            'Host' : 'movie.douban.com'
                }
    movie_list = []

    for i in range(0 ,10):
        link = 'http://movie.douban.com/top250?start=' +str(i * 25) + "&filter="
        r = requests.get(link ,headers = headers ,timeout = 10)
        print(str(i+1),"页码响应状态:" ,r.status_code)
        
        soup = BeautifulSoup(r.text ,"html.parser")
        div_list = soup.find_all('div' ,class_= 'hd')
        for each in div_list:
            movie = each.a.span.text.strip()
            movie_list.append(movie)


    return movie_list

movies = get_movies()
print(movies)
