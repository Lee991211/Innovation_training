# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Author   : 汪逢生
# @FILE     : all.py
# @Time     : 2020/6/7 11:30
# @Software : PyCharm

from crawler import toutiao
import pymysql

db = pymysql.connect(host="localhost", port=3308,user="root", passwd="",database="toutiao")
cursor = db.cursor()


def  test():
    # query = input('请输入想要查询的东西')
    query = '特朗普'
    toutiaocrawler = toutiao.toutiaocrawler()
    # # cookie = input('请输入cookie')
    # # toutiaocrawler.set_cookie(cookie)
    all_list = toutiaocrawler.main(query)
    try:
        cursor.execute('''DROP TABLE IF EXISTS toutiao''')
        cursor.execute('''create table IF NOT EXISTS  toutiao (id INT PRIMARY KEY AUTO_INCREMENT,content  Text not null ,comment_time Text not null,comment Text )''')
        cursor.execute('''alter table toutiao convert to character set utf8''')
        for i in all_list:
            try:
                if len(i[2]) == 0:
                    sql = "INSERT INTO toutiao(content,comment_time,comment) VALUES ('%s', '%s', '%s')" % (i[0], i[1], "")
                    cursor.execute(sql)
                else:
                    for z in i[2]:
                        sql = "INSERT INTO toutiao(content,comment_time,comment) VALUES ('%s', '%s', '%s')" % (i[0], i[1], z)
                        cursor.execute(sql)
            except:
                continue
    except:
        print("...mysql error")
        db.rollback()


    db.close()

if __name__ == '__main__':
    test()