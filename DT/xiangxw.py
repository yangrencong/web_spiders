import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import time
import csv
headers = {
        'User-Agent': 
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
            }


#获得所需网页的进入附加id
def get_id():

    options = webdriver.firefox.options.Options()
    driver = webdriver.Firefox(executable_path='D:/Python36/geckodriver',firefox_options=options)
    spiderurl = "http://gxw.xa.gov.cn/ptl/def/def/index_1263_1787_ci_trid_3719953.html"
    driver.get(spiderurl)
    content = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(content, 'lxml')
    title_list = soup.find_all('div' ,class_ = 'dTreeNode')
    title_id_list = []
    for title in title_list:
        title_id = title.find('a') #找出所有包含文章id的a标签语句
        title_id = re.findall( r"\d+", str(title_id) )
        try:
         each_id = title_id[3]    
        except IndexError:
            pass
        else:
            title_id_list.append(each_id)
            #注意此附加id中有错误id，需在后续中继续甄别
            #后续发现有错误id也没有bug，错误id下的网页依然存在，只是没有数据，并不妨碍爬取

    #print(len(title_list))
    #with open("gxw_html.txt" ,"a+") as f_obj:
    #    f_obj.write(soup.prettify())
    #    f_obj.close
    #print(soup.prettify())
    driver.quit()
    print(title_id_list)
    return title_id_list

#当内容页数超过一页时调用此模块
def get_other_q_num(ids ,page):
    all_q_num = [ ]
    data = {
            "hidden_CiDataTable":	        "UT_CAT_MDDATA",
            "hidden_UT_CAT_MDDATA_CiEditMode":   "null",
            "hidden_UT_CAT_MDDATA_CiTableMan":	"null",
            "hidden_UT_CAT_MDDATA_CiTrid":	"null",
            "hidden_UT_CAT_MDDATA_intoTop":	"null",
            "hidden_UT_CAT_MDDATA_PageCount":	"19",
            "hidden_UT_CAT_MDDATA_PageNumber":	str(int(page)-1),
            "hidden_UT_CAT_MDDATA_PagerCmd":	" ",
            "hidden_UT_CAT_MDDATA_pindex":	page,
            "hidden_UT_CAT_MDDATA_RowCount":	"15"
            }
    url = "http://gxw.xa.gov.cn/ptl/def/def/index_1263_1790.jsp?recid=" + str(ids) +"&_cimake=false&pageNumber=" + str(page) +".html"
    print(url)
    r = requests.post(url ,data = data)
    #time.sleep(1)
    print(r.status_code)
    soup = BeautifulSoup(r.text ,'lxml')
    #print(soup.prettify())
    title_contents = soup.find_all("td" ,class_ = "shuzi")
    for title_content in title_contents:
        q_num = title_content.text.strip()
        all_q_num.append(q_num[16:])
    return all_q_num



#解决列表的嵌套的问题
def splitlist(list):
    '''
        现有一个列表，里面元素包括 数字，字母，列表，字典等元素，现在要将字典去掉，并将列表
        分解成字母，或数字元素如：[[1,2,3],2,3,[1,3,[12,22]],'a',12] 
        经函数处理后[1, 2, 3, 2, 3, 1, 3, 12, 22, 'a', 12]
        
    '''    
    alist = []
    a = 0
    
    for sublist in list:
        if isinstance(sublist,str) != True:
            try: #用try来判断是列表中的元素是不是可迭代的，可以迭代的继续迭代
                for i in sublist:
                    alist.append (i)
            except TypeError: #不能迭代的就是直接取出放入alist
                alist.append(sublist)
        else:
             alist.append(sublist)

    for i in alist:
        if type(i) == type([]):#判断是否还有列表
            a =+ 1
            break
    if a==1:
        return splitlist(alist) #还有列表，进行递归
    if a==0:
        return alist

def write_to_csv(lists , method):
    with open("data.csv" , method ,encoding = "UTF-8" ,newline = '') as csv_f:
        w = csv.writer(csv_f)
        w.writerow(lists)
    return


ids_list = get_id() #获得每个小选项的附加id
q_num_list = [ ]    #每一个小选项的的索引号列表
for ids in ids_list:

    url ='http://gxw.xa.gov.cn/ptl/def/def/index_1263_1790_ci_recid_' + str(ids) +".html"
    #url = "http://gxw.xa.gov.cn/ptl/def/def/index_1263_1790_ci_recid_3719959.html"
    print(url)
    r = requests.get(url ,headers = headers)
    #time.sleep(1)
    print(r.status_code)
    soup = BeautifulSoup(r.text ,'lxml')
    #print(soup.prettify())
    title_contents = soup.find_all("td" ,class_ = "shuzi")
    for title_content in title_contents:
        q_num = title_content.text.strip()
        q_num_list.append(q_num[16:])
        #print(q_num[16:])
    #print(title_contents)
    pagecount = soup.find("span" ,class_ = "pageCount").text.strip()
    pagecount =int(''.join(re.findall( r"\d+",pagecount)))
    if pagecount == 1:
        pass
    else:
        for page in range(1 ,pagecount):
            oth_q_num = get_other_q_num(ids ,page)
            q_num_list.append(oth_q_num)
    

q_num_list = splitlist(q_num_list)  #将内嵌列表完全打开
print(len(q_num_list))
q_num_list = list(filter(None ,q_num_list))#去除列表中的空字符
print(len(q_num_list))
#到此处已完成所需网页的所有信息，只需爬取即可
q_num_list = {}.fromkeys(q_num_list).keys()  #去除重复项
print(len(q_num_list))

#最终内容的爬取，并存入csv，并将大段内容作为txt，制作索引
item_list =    ["文件题目",
                "发布机构",
                "发布时间",
                "索 引 号",
                "关 键 字",
                "主题分类",
                "内容.txt"
                           ]

write_to_csv(item_list , "w+")

content_list = []
for q_num in q_num_list:
    url2 = "http://gxw.xa.gov.cn/websac/cat/" + str(q_num) + ".html"
    #url2 = "http://gxw.xa.gov.cn/ptl/def/def/index_1263_1361_ci_trid_" + q_num +".html"
    r2 = requests.get(url2 ,headers = headers)
    soup2 = BeautifulSoup(r2.text ,"html.parser")
    print(url2)
    print(r2.status_code)
    try:
        title = soup2.find("div" ,id = "divTitle").text.strip()
        content_list.append(title)
        topics = soup2.find("div" ,id = "divTopicInfo").find_all("td")
        for topic in topics:
            topic = topic.text.strip()
            content_list.append(topic[6:])
        divcontent = soup2.find("div" ,id = "divContent").text.strip()
        content_list.append(q_num + ".txt")
        write_to_csv(content_list ,"a+")
        content_list.clear()
        #对txt文件进行命名
        file_name = "C:\\Users\\Administrator\\Desktop\\DT\\txt\\" + q_num + ".txt" 
        with open(file_name ,"a+",encoding='utf-8') as f_obj:
            f_obj.write(divcontent)
            f_obj.close()

    except AttributeError:
        div_content = soup2.text.strip()
        with open(q_num +".txt" ,"a+" ,encoding = 'utf-8')as f_obj:
            f_obj.write(div_content)
            f_obj.close()


















