# coding=gbk
import re
m = re.match('www' ,'www.santotangs.com')
print("匹配的结果：" ,m)
print("匹配的起点和终点" ,m.span())
print("匹配的起点位置" ,m.start())
print("匹配的终点位置" ,m.end())
