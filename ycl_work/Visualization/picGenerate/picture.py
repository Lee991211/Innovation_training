# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 09:59
# @Author  : 尹成林
# @Site    : https://me.csdn.net/sdyinruichao
# @File    : picture.py
# @Software: PyCharm

import sys
import numpy as np
sys.path.append("..")
from Visualization.picGenerate.Bar import *
from Visualization.picGenerate.Line import *
from Visualization.picGenerate.WordCloud import *
from Visualization.dataProsc.dataPro import *
from Visualization.utils.setting import *


def weibo_m_emo(key):
    t = str(0)
    sheetname = "emotion_val"
    data = dataForPridic(sheetname, sheetname, t, key)
    print(len(data))
    x = []
    for i in day:
        xx = []
        for ii in range(i):
            xx.append(ii)
        x.append(xx)
    y = []
    n = [2, 3, 4, 5]
    p = 0
    for i in day:
        y1 = []
        for ii in range(i):
            y1.append(data[p+ii])
        y.append(y1)
        p = p + i
    # print(y)
    pic = []
    for i in range(len(y)):
        kk = []
        kk.append(y[i])
        k = []
        k.append(n[i])
        kkk = Getline(x[i], kk, k)
        pic.append(kkk)
    return pic


def weibo_predict(key):
    name = 'emotion_val'
    data = dataForPridic(name, name, 1, key)
    n = [6]
    y = []
    x = []
    y.append(data)
    for i in range(30):
        x.append(i)
    pic = Getline(x, y, n, '(预测)')
    return pic


def weibo_bodong(key):
    t = str(0)
    sheetname = "emotion_val"
    data = dataForPridic(sheetname, sheetname, t, key)
    print(len(data))
    x = []
    for i in range(32):
        x.append(i)
    y = []
    n = ['2月',
         '3月',
         '4月',
         '5月']
    p = 0
    for i in day:
        y1 = []
        for ii in range(i):
            y1.append(float(data[p + ii]))
        y.append(y1)
        p = p + i
    d = []
    d1 = []
    for i in range(len(y)):
        print(i)
        d.append(np.var(y[i]))
        d1.append(np.mean(y[i]))
    print(d)
    dd = []
    dd.append(d)
    dd.append(d1)
    strr = ['月份情感标准差', '月份情感平均值']
    pic = getBar(n, dd, strr, "舆情波动与平均情况")
    return pic


def wc(key, plat):
    filename = '{}/{}.csv'.format(plat, key)
    data = dataForWordCloud(filename)
    pic = getWordCloud(data, pingtai[plat])
    return pic


def wordcloud(key):
    pic = []
    for i in plats:
        kkk = wc(key, i)
        pic.append(kkk)
    return pic


def weiboredian(key):
    kkk = getWeiboTop(key)
    return kkk


if __name__ == "__main__":
    a = 'toutiao'
    print(pingtai[a])
    wordcloud('trump')
