# -*- coding: utf-8 -*-
# @Time    : 2020/6/18 9:02
# @Author  : 尹成林
# @Site    : https://me.csdn.net/sdyinruichao
# @File    : setting.py
# @Software: PyCharm
import sys
sys.path.append("..")

# mysql具体设置
mysqlbase = {
    'address': 'linmumu.online',
    'port': 3306,
    'user': 'test',
    'password': '123456',
    'using': 'innotrain',
    'charset': 'utf8'
}

# 读写相关文件文件的存储目录
FileReadPath = 'Visualization/data/source/'
FileRTPath = 'Visualization/data/target/'
FileFeaturePath = "Visualization/data/feature/baidu_stopwords.txt"


# 打印当前所有设置
def settinghelp():
    print('Mysql setting:   {}'.format(mysqlbase))
    print("FileReadPath:    {}".format(FileReadPath))
    print("FileR&TPath:    {}".format(FileRTPath))
    print("FileFeaturePath:    {}".format(FileFeaturePath))


# picture.py使用的相关生成的使用的变量
day = [29, 31, 30, 31]
pingtai = {
    'zhihu': '知乎',
    'weibo': '微博',
    'toutiao': '头条'
}
plats = ['zhihu', 'weibo', 'toutiao']

