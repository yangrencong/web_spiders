#coding = UTF-8
import MySQLdb

conn = MySQLdb.connect(
        host = 'localhost' ,
        user = 'root', 
        passwd = '1452581359',
        db = 'scraping')
cur = conn.cursor()
cur.execute("INSERT INTO urls (url, content) VALUES('www.baidu.com' ,'This is content')" )
cur.close()
conn.commit()
conn.close()
