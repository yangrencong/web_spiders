from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import re



options = webdriver.firefox.options.Options()

driver = webdriver.Firefox(executable_path='D:/Python36/geckodriver',firefox_options=options)
for i in range(0,18):

    spiderurl="https://zh.airbnb.com/s/Shenzhen--China/homes?refinement_paths%5B%5D=%2Fhomes&cdn_cn=1&allow_override%5B%5D=&s_tag=CrHRSvZj&section_offset=" + str(i)
    driver.get(spiderurl)
    rent_list = driver.find_elements_by_css_selector('div._v72lrv')
    
    print("第"+str(i)+"页响应成功")
    #comments = []
    for eachhouse in rent_list:
        
        print(eachhouse)
        house_name = eachhouse.find_element_by_css_selector('div._190019zr')
        house_name = house_name.text
        print(house_name)
        house_type = eachhouse.find_element_by_css_selector('div._1etkxf1')
        house_type = house_type.text
        print(house_type)
        house_price = eachhouse.find_element_by_css_selector('div._1yarz4r')
        house_price = house_price.text.strip("每晚\n价格\n")
        print(house_price)
        house_comment = eachhouse.find_element_by_css_selector('span._1cy09umr')
        house_comment = house_comment.text
        print(house_comment)
        #获取star
        complete_stars = eachhouse.find_elements_by_class_name("_19olcgv7")
        complete_stars = len(complete_stars)
        try:
            half_star = eachhouse.find_element_by_class_name("_1ir1ce4u")
            
        except NoSuchElementException:
            half_star = 0
        else:
            half_star = 0.5
        
        stars_comment = complete_stars + half_star 
        print(stars_comment)
        #half_star = eachhouse.find_element_by_class_name

    #print(house_price + house_information)
    #comments.append(comment)
    #print(comments)
    #print(len(comments))
driver.quit()


