#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Mr.yang
# Created Time : 2018/10/11 星期四 10:14:03
# File Name: mutext.py
# Description:
# Editortool: vim8.0
"""
from multiprocessing import Process, Queue
import time
import requests

link_list = []
with open('alexa.txt', 'r') as file:
    file_list = file.readlines()
    for eachone in file_list:
        link = eachone.split('\t')[1]
        link = link.replace('\n', '')
        link_list.append(link)

start = time.time()


class MyProcess(Process):
    def __init__(self, q):
        Process.__init__(self)
        self.q = q

    def run(self):
        print("Starting ", self.pid)
        while not self.q.empty():
            crawler(self.q)
        print("Exiting ", self.pid)


def crawler(q):
    url = q.get(timeout=2)
    try:
        r = requests.get(url, timeout=20)
        print(q.qsize(), r.status_code, url)
    except Exception as e:
        print(q.qsize(), url, 'Erorr: ', e)


if __name__ == '__main__':
    ProcessNames = ["Process-1", "Process-2", "Process-3"]
    workQueue = Queue(1000)
    proc_record = []

    # 填充队伍
    for url in link_list:
        workQueue.put(url)
       
    for i in range(0, 100):
        print(i)
        p = MyProcess(workQueue)
        p.daemon = True
        p.start()
        proc_record.append(p)

    p.join() 

    end = time.time()
    print("Process + Queue 多线程爬虫的总时间为：", end-start)
    print("Main process Ended!")





