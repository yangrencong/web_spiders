from selenium import webdriver




#将上面位置修改为计算机中firefox程序的地址
options = webdriver.firefox.options.Options()
driver = webdriver.Firefox(executable_path='D:\Python36\geckodriver', firefox_options=options)
driver.get("https://www.baidu.com")

