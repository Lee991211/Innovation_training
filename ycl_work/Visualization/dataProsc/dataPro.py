# -*- coding: utf-8 -*-
# @Time1    : 2020/6/29 09:12
# @Author  : 尹成林
# @Site    : https://me.csdn.net/sdyinruichao
# @File    : dataPro.py
# @Software: PyCharm

import sys
sys.path.append("..")
from Visualization.utils.common import *
from Visualization.dataProsc.readDbs import *


def dataForPridic(mql_sheet, data_name, data_n=30):
    mql = "select {} from {} limit 0, {}".format(data_name, mql_sheet, data_n)
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


if __name__ == "__main__":
    print("dataPro正常运行")
    data = dataForPridic('emotion_val', 'emotion_val')
    print(data)
