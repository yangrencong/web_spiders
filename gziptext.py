import requests
import chardet

url = 'http://www.sina.com.cn/'
r = requests.get(url)
print(r.text)
after_gzip = r.content
print('解压后字符串编码为：', chardet.detect(after_gzip))
print(after_gzip.decode("UTF-8"))
