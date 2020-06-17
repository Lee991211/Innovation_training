# -*- coding: utf-8 -*-
# @Time    : 2020/6/8 9:00
# @Author  : 尹成林
# @Site    : https://me.csdn.net/sdyinruichao
# @File    : read_file.py
# @Software: PyCharm

import os
import time
import csv


# 加载csv使用
def load_csv(name):
    f = csv.reader(open(name, 'r'))
    dataset = list(f)
    return dataset


# 加载文件后缀名
def get_file_type(filename):
    a = os.path.splitext(filename)[-1]
    return a.split('.')[1]


# 查找某目录下所有文件返回文件名
def scan_files(directory, files_list, prefix=None, postfix=None):
    list = []
    for fpath, dirname, fnames in os.walk(directory):
        for i in fnames:
            if str(i) not in files_list:
                list.append(str(i))
                files_list.append(str(i))
    return list


def test_read_file():
    list = []
    while True:
        time.sleep(1)
        ll = scan_files("data/Raw_data", list)
        print(ll)
        for i in ll:
            print(get_file_type(i))


test_read_file()
