# -*- coding: utf-8 -*-
# @Time1    : 2020/6/19 19:02
# @Time2    : 2020/6/20 15:02
# @Author  : 尹成林
# @Site    : https://me.csdn.net/sdyinruichao
# @File    : readDbs.py
# @Software: PyCharm
import pymysql
import sys
import csv
import numpy as np
sys.path.append("..")
from Visualization.utils.setting import *



# 数据库的读取
class DbReader:
    conn = pymysql.connect(
        host=mysqlbase['address'],
        port=mysqlbase['port'],
        user=mysqlbase['user'],
        password=mysqlbase['password'],
        db=mysqlbase['using'],
        charset=mysqlbase['charset']
    )

    def __init__(self):
        print("新建DbReader成功")

    # 测试连接是否可用
    def ConTest(self, i=0):
        # conn = pymysql.connect(host='47.98.141.4', user='test', password='123456', db='innotrain', port=3306)
        try:
            self.conn.ping()  # 采用连接对象的ping()函数检测连接状态
            print('Connect-%d ok' % i)
            return 1
        except Exception as ex:
            print("Disconnect reason:{}".format(ex))
            return -1

    # 读取预测后的结果
    def ReadData(self, sql):
        try:
            c = self.conn
            cur = c.cursor()
            cur.execute(sql)
            u = cur.fetchall()
            return u
        except Exception as ex:
            print("sql is wrong! Bc:{}".format(ex))
            return -1


class ReadCsv:
    FileReadPath = FileReadPath

    def loadcsv(self, name):
        try:
            f = csv.reader(open("{}{}".format(self.FileReadPath, name), 'r'))
            dataset = list(f)
            return dataset
        except Exception as ex:
            print("LOAD IS WRONG! Bc:{}".format(ex))
            return int(-1)

    # data数据格式为list类型
    def writecsv(self, name, data):
        try:
            np.savetxt('{}{}.csv'.format(self.FileReadPath, name), data, delimiter=',', fmt='%f')
            return 1
        except Exception as ex:
            print("WRITE IS WRONG! Bc:{}".format(ex))
            return -1


if __name__ == "__main__":
    settinghelp()
    a = DbReader()
    DbReader.ConTest(a)
    a.ReadData('select * from emotion_val')
