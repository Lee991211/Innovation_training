# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 09:59
# @Author  : 尹成林
# @Site    : https://me.csdn.net/sdyinruichao
# @File    : Line test.py
# @Software: PyCharm

import sys
sys.path.append("..")
from Visualization.picGenerate.Line import GetLine
from Visualization.dataProsc.readDbs import *
from Visualization.dataProsc.dataPro import dataForPridic


def testcsv():
    a = ReadCsv()
    csv1 = a.loadcsv("result.csv")
    csv2 = a.loadcsv("result3.csv")
    x = []
    for i in range(32):
        x.append(i)
    y1 = []
    y2 = []
    for i in range(len(csv1)):
        if i != 0:
            y1.append(csv1[i][1])
    for i in csv2:
        y2.append(i[1].split('.')[0] + '.' + str(i[1]).split('.')[1][:2])
    y = []
    y.append(y1)
    y.append(y2)
    print(y)
    n = [1, 3]
    GetLine(x, y, n)


def testmysql():
    name = 'emotion_val'
    data = dataForPridic(name, name)
    y = []
    x = []
    y.append(data)
    for i in range(30):
        x.append(i)
    n = [5]
    GetLine(x, y, n)


testmysql()

