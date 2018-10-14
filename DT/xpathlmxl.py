import requests
from lxml import etree

link = "http://www.santostang.com/"
headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36",
        "Host":
        "www.santostang.com"
        }
r = requests.get(link ,headers = headers)
html = etree.HTML(r.text)
title_list = html.xpath('//h1[@class = "post-title"]/a/text()')
infor_list = html.xpath('//*[@id="main"]/div/div[1]/article[2]/div/p/text()')
print(title_list)
print(infor_list)
#//*[@id="main"]/div/div[1]/article[4]/div/p
#//*[@id="main"]/div/div[1]/article[5]/div/p
#//*[@id="main"]/div/div[1]/article[1]/div/p

for i in range(1,6):
    infor_l = html.xpath('//*[@id="main"]/div/div[1]/article[' + str(i) +']/div/p/text()') #次数返回的事字符串
    infor_s = ''.join(infor_l)  #此处将列表转换为字符串
    print("第%s项："%(i) )
    print(infor_s)

