# -*- coding: utf-8 -*-
# @Time    : 2020/6/18 9:02
# @Author  : 尹成林
# @Site    : https://me.csdn.net/sdyinruichao
# @File    : setting.py
# @Software: PyCharm
import json
import re


# list --> dict
def ListToDict(a, b):
    c = zip(a, b)
    return c


# dict --> list
def DictToList(a, i):
    if i == 0:
        b = list(a)
    elif i == 1:
        b = list(a.value)
    return b


# json <--> dict
def JsonToDict(a):
    b = json.load(a)
    return b


def DictToJson(a):
    b = json.dump(a)
    return b


# 保留两位小数
def KeepTwo(a):
    if len(a)>2:
        return a.split('.')[0] + '.' + str(a).split('.')[1][:2]
    else:
        return a


# 去除掉汉字
def find_unchinese(file):
    pattern = re.compile(r'[\u4e00-\u9fa5]')
    unchinese = re.sub(pattern, "", file)
    print(unchinese)

