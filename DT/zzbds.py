#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Mr.yang
# Created Time : 2018/9/16 星期日 17:05:42
# File Name: zzbds.py
# Description:
"""
import requests
import re

link = "http://www.santostang.com/"
headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
        'Host':
        'www.santostang.com'
        }
r = requests.get(link ,headers = headers)
html = r.text
print(html)
title_list = re.findall('<h1 class="post-title"><a href=.*?>(.*?)</a></h1>',html)
print(title_list)
