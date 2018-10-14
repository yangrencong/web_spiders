#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Mr.yang
# Created Time : 2018/9/12 星期三 9:35:40
# File Name: Top250.py
# Description:爬取豆瓣250的榜单资料
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
def get_movies_name():
    headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/68.0.3440.84 Safari/537.36',
            'Host' : 'movie.douban.com'
                }

    movies_chinese_name_list = []
    movies_english_name_list = []
    movies_other_name_list = []
    
    for j in range(0 ,10):
        
        i = 25 * j
        link = 'http://movie.douban.com/top250?start=' + str(i) + "&filter= "
        r = requests.get(link ,headers = headers ,timeout = 10)
        print(str(j+1) ,"页响应代码" , r.status_code)
        soup = BeautifulSoup(r.text ,"html.parser")
        div_list = soup.find_all('div' ,class_ = 'hd')
        for each in div_list:
            #each.a.span只会定位到a标签下的第一个标签的内容
            #each.a.contents会定位到a标签下的每一个标签的内容
            #print(len(each.a.contents))
            #movie_chinese=each.a.span.text.strip()
            #第一个为0.
            movie_chinese = each.a.contents[1].text.strip()

            movie_english = each.a.contents[3].text.strip() #此处打印有前置空格
            movie_english = movie_english[2:] #去除该名称前的两个空格
            #其他名字存储在第6个内容，但可能不存在，故需要判断
            #内容编号从0开始，有些内容中没有数据，故若没有需判断，避免出错
            if len(each.a.contents) > 5:
                movie_other_name = each.a.contents[5].text.strip()
                #print(movie_other_name)

            movies_chinese_name_list.append(movie_chinese)
            movies_english_name_list.append(movie_english)
            movies_other_name_list.append(movie_other_name.strip("/"))

    return movies_chinese_name_list ,movies_english_name_list ,movies_other_name_list
 

def get_other_contents():
    headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/68.0.3440.84 Safari/537.36',
            'Host' : 'movie.douban.com'
                }

    directors_list = []
    starring_list = []
    movie_release_date_list = []
    movie_country_list = []
    movie_classfication_list = []
    for j in range(0 ,10):
        i = 25 * j
        link = 'http://movie.douban.com/top250?start=' + str(i) + "&filter= "
        r = requests.get(link ,headers = headers ,timeout = 10)
        print(str(j+1) ,"页响应代码" , r.status_code)
        soup = BeautifulSoup(r.text ,"html.parser")
        div_list = soup.find_all("div" ,class_ = 'bd')
        for each in div_list:
            if len(each.p.contents) > 1:
                #此处爬到的数据为电影的年份，国家，类别信息
                movie_information = each.p.contents[2].strip()
                #对字符串进行分割，分割记号为“/”
                movie_information = movie_information.split('/')
                movie_release_date_list.append(movie_information[0].strip("\xa0"))
                movie_country_list.append(movie_information[1].strip(" "))
                movie_classfication_list.append(movie_information[2].strip(" "))
                
                #print(each.p.contents[0].strip())
                #84句注意打印的导演与主演之间的空格数，否则切片字符串会错误
                each_movie = each.p.contents[0].strip().split("   ")
                director = each_movie[0]
                #此处存在问题，动画电影中有导演而无演员
                if len(each_movie) > 1:
                    starring = each_movie[1]
                #去掉多余的字符（导演：）
                directors_list.append(director.strip("导演:"))
                starring_list.append(starring.strip("主演:").strip(".").strip("/"))
    return directors_list ,starring_list ,movie_release_date_list ,movie_country_list ,movie_classfication_list

def get_movie_score():
    #获得电影评分和一句话描述电影
    headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/68.0.3440.84 Safari/537.36',
            'Host' : 'movie.douban.com'
                }
    movie_score_list = []
    movie_review_list = []
    movie_comment_num_list = []
    for j in range(0 ,10):
        i = 25 * j
        link = 'http://movie.douban.com/top250?start=' + str(i) + "&filter= "
        r = requests.get(link ,headers = headers ,timeout = 10)
        print(str(j+1) ,"页响应代码" , r.status_code)
        soup = BeautifulSoup(r.text ,"html.parser")
        div_list1 = soup.find_all("div" ,class_ = 'star')
        div_list2 = soup.find_all("p" ,class_ = 'quote')
        for each_1 in div_list1:
            #可用此句来找到究竟该内容中有多少项内容，并寻找自己想要的信息
            #print(len(each_1.contents))
            #for k in range(0 ,9):
            #   print( str(k) +str(each_1.contents[k]))
            movie_score = each_1.contents[3].text
            movie_score_list.append(movie_score)
            movie_comment_num = each_1.contents[7].text.strip("人评价")
            movie_comment_num_list.append(movie_comment_num)
            
        for each_2 in div_list2:
            movie_review = each_2.text.strip()
            movie_review_list.append(movie_review)
    return movie_score_list ,movie_comment_num_list ,movie_review_list













(movies_name_chn ,movies_name_eng ,movies_name_oth) = get_movies_name()
(directors_list ,starring_list ,movie_release_date_list ,movie_country_list ,movie_classfication_list)=get_other_contents()
(movie_score_list ,movie_comment_num_list ,movie_review_list) = get_movie_score()

DT_list = [
        movies_name_chn ,
        movies_name_eng ,
        movies_name_oth ,
        directors_list ,
        starring_list ,
        movie_release_date_list ,
        movie_country_list ,
        movie_classfication_list ,
        movie_score_list ,
        movie_comment_num_list ,
        movie_review_list
        ]

DT_list = (list(map(list ,zip(*DT_list))))
print(DT_list)
name = [
        "电影中文名",
        "电影中文名",
        "电影其它名称",
        "导演",
        "主演",
        "首映日期",
        "国家",
        "类型",
        "豆瓣评分",
        "评论人数",
        "一句话影评"
        ]
DB250_Data = pd.DataFrame(columns = name ,data = DT_list)
DB250_Data.to_csv("C:/Users/Administrator/Desktop/DT/DT250.csv")

#print(movie_review_list)
#打印每个列表的长度意义在于可以迅速的匹配信息
#print(len(directors_list))
#print(len(starring_list))
#print(len(movies_name_chn))
#print(len(movies_name_eng))
#print(len(movies_name_oth))
#print(len(movie_score_list))
#print(len(movie_comment_num_list))
#print(len(movie_review_list))





