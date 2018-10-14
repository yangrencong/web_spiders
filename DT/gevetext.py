#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Mr.yang
# Created Time : 2018/10/13 星期六 12:37:08
# File Name: gevetext.py
# Description:
# Editortool: vim8.0
"""
import gevent
from gevent.queue import Queue, Empty
import time
import requests

# 引入猴子补丁
from gevent import monkey 
# 将所有需要调用的库的阻塞式系统调用
monkey.patch_all()
# 例如这里设置为一百万


link_list = []
with open('alexa.txt', 'r') as file:
    file_list = file.readlines()
    for eachone in file_list:
        link = eachone.split('\t')[1]
        link = link.replace('\n', '')
        link_list.append(link)

start = time.time()


def crawler(index):
    Process_id = 'Process-' + str(index)
    while not workQueue.empty():
        url = workQueue.get(timeout=2)
        try:
            r = requests.get(url, timeout=20)
            print(Process_id, workQueue.qsize(), r.status_code, url)
        except Exception as e:
            print(Process_id, workQueue.qsize(), url, 'Erorr: ', e)


def boss():
    for url in link_list:
        workQueue.put_nowait(url)


if __name__ == '__main__':
    workQueue = Queue(1000)
    gevent.spawn(boss).join()
    jobs = []
    for i in range(10):
        jobs.append(gevent.spawn(crawler, i))

    gevent.joinall(jobs)
    end = time.time()
    print('gevent + Queue 多协程爬虫的总时间： ', end-start)
    print('Main Ended')



