#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Mr.yang
# Created Time : 2018/10/11 星期四 18:36:51
# File Name: pool+que.py
# Description:
# Editortool: vim8.0
"""
from multiprocessing import Pool, Manager
import time
import requests

link_list = []
with open("alexa.txt", "r") as f_obj:
    file_list = f_obj.readlines()
    for eachone in file_list:
        link = eachone.split('\t')[1]
        link = link.replace('\n', "")
        link_list.append(link)

start = time.time()


def crawler(q, index):
    Process_id = 'Process-' + str(index)
    while not q.empty():
        url = q.get(timeout=2)
        try:
            r = requests.get(url, timeout=20)
            print(Process_id, q.qsize(), r.status_code, url)
        except Exception as e:
            print(Process_id, q.qsize(), url, 'Erorr: ', e)


if __name__ == "__main__":
    manager = Manager()
    workQueue = manager.Queue(1000)

    # 填充队伍
    for url in link_list:
        workQueue.put(url)

    pool = Pool(processes=50)
    for i in range(10):
        pool.apply_async(crawler, args=(workQueue, i))

    print("Started processes")
    pool.close()
    pool.join()

    end = time.time()
    print('Pool + Queue多进程爬虫的总时间： ', end-start)
    print('Main Process Ended')


