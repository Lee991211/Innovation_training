# -*- coding: utf-8 -*-
# @Time1    : 2020/6/29 09:12
# @Author  : 尹成林
# @Site    : https://me.csdn.net/sdyinruichao
# @File    : dataPro.py
# @Software: PyCharm

import sys
import jieba
import jieba.analyse
from operator import itemgetter
import re
sys.path.append("..")
from Visualization.utils.common import *
from Visualization.dataProsc.readDbs import *
from Visualization.utils.setting import FileFeaturePath


# k表示预测还是实际
def dataForPridic(mql_sheet, data_name, k, key):
    print(key)
    a = str(key)
    mql = "select {} from {} where topic = '{}' and predict = {}".format(data_name, mql_sheet, a, k)
    mysql = DbReader()
    a = mysql.ConTest()
    if a == -1:
        return -1
    else:
        datas = mysql.ReadData(mql)
        ppp = []
        for i in datas:
            ppp.append(KeepTwo(i[0]))
        return ppp


"""
#wordcloud相关
"""


# name为文件名称， key为关键字
def dataForWordCloud(name, key = ''):
    inputs = readTxt(name)
    jieba.analyse.set_stop_words(FileFeaturePath)
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    outputs = ""
    for line in inputs:
        output = re.sub(pattern, "", line)
        seg = jieba.cut(output.strip(), cut_all=False)
        # 分好词之后之间用空格隔断
        output = ' '.join(seg)
        outputs = outputs + str(output)
    # print(outputs)
    keywords = jieba.analyse.extract_tags(outputs, topK=30, withWeight=True, allowPOS=())
    # print(keywords)
    return keywords


def getWeiboTop(name):
    filename = "weibo/{}.csv".format(name)
    data = list(readTxt(filename))
    data1 = []
    for i in range(len(data)):
        try:
            if i != 0:
                data1.append(data[i].split(','))
        except Exception as ex:
            print(i)
            continue
    pic = []
    for i in range(5):
        kkk = []
        kkk.append(data1[i][3])
        kkk.append(data1[i][4])
        pic.append(kkk)
    print(pic)
    return pic


if __name__ == "__main__":
    getWeiboTop('trump')

