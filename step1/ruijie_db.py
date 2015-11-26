# encoding: gbk
"""
@version: 1.0
@author: pierre94
@license: Apache Licence 
@contact: admin@bear2.cn
@site: www.bear2.cn
@software: PyCharm Community Edition
@file: ruijie_db.py
@time: 2015/11/26 15:12
"""
import MySQLdb
import sys
def connect():
    try:
        #mysql账户密码
        conn=MySQLdb.connect(host="localhost",user="root",passwd="PasswordForTest",db="ruijie")
        print "连接成功,from ruijie_db"
        return conn
    except Exception,e:
        print "连接错误"
        print e
        sys.exit()

def select_user():
    conn=connect()
    cursor=conn.cursor()
    sql1="select * from users order by uid"
    cursor.execute(sql1)
    data=cursor.fetchall()
    return data

def insert_data():
    #将数据存入输入数据库
    pass




