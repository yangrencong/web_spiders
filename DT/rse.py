#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Mr.yang
# Created Time : 2018/9/11 星期二 13:08:35
# File Name: re.py
# Description:
"""
import requests
key_dict = {
        'key1' :'value1' ,
        'key2' :'value2'
        }
headers = {
        'user-agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
        'Host' :'www.santostang.com'
        }
r = requests.get('http://www.santostang.com' ,headers = headers)
print("url已经正确编码：" ,r.url )
print("响应状态码：" ,r.status_code)
