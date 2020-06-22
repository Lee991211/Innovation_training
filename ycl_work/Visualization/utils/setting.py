# -*- coding: utf-8 -*-
# @Time    : 2020/6/18 9:02
# @Author  : 尹成林
# @Site    : https://me.csdn.net/sdyinruichao
# @File    : setting.py
# @Software: PyCharm

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
FileReadPath = '../data/source/'
FileRTPath = '../data/target/'
FileFeaturePath = "../data/feature/"


# 打印当前所有设置
def settinghelp():
    print('Mysql setting:   {}'.format(mysqlbase))
    print("FileReadPath:    {}".format(FileReadPath))
    print("FileR&TPath:    {}".format(FileRTPath))
    print("FileFeaturePath:    {}".format(FileFeaturePath))

