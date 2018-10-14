import requests
from bs4 import BeautifulSoup
import datetime

def get_page(link):
    headers = {
            'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
            }
    r = requests.get(link ,headers = headers )

    print(r.status_code)

    html = r.content
    html = html.decode("UTF-8")
    soup = BeautifulSoup(html ,"lxml")
    
    return soup

def get_data(post_list):
    data_list = []
    for post in post_list:
        title_td = post.find('div' ,class_ = "title box")
        title = title_td.find('a' ,id = True).text.strip()
        print(title)
        post_link = title_td.find('a' ,id= True)['href']
        post_link = "https://bbs.hupu.com" + post_link
        print(post_link)
        




link = "https://bbs.hupu.com/bxj"
soup = get_page(link)
post_list = soup.find_all('div' ,class_ = 'show-list')
print(post_list)
get_data(post_list)
#data_list = get_data(post_list)

