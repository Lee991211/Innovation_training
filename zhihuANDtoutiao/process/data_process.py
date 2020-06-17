# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Author   : 汪逢生
# @FILE     : data_process.py
# @Time     : 2020/6/6 1:33
# @Software : PyCharm

import  pandas as pd


def process():
    file = pd.read_csv("../data/toutiao/新冠疫情.txt")
    print(file['time'])
    # for i in file['time']:
    #     print(i)


if __name__ == '__main__':
    process()