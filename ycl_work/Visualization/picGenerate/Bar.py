# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 15:02
# @Author  : 尹成林
# @Site    : https://me.csdn.net/sdyinruichao
# @File    : readDbs.py
# @Software: PyCharm

import sys
import jieba
import jieba.analyse
import re
from pyecharts.charts import Bar
import pyecharts.options as opts
from pyecharts.globals import ThemeType
sys.path.append("..")
from Visualization.dataProsc.readDbs import *


def getBar(dataX, dataY,n, T=""):
    theBar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC))
        .add_xaxis(dataX)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="{}".format(T)),
            toolbox_opts=opts.ToolboxOpts(is_show=True),

        )
    )
    for i in range(len(dataY)):
        theBar.add_yaxis('{}'.format(n[i]), dataY[i], label_opts=opts.LabelOpts(is_show=False),

                        # markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"), ]), is_smooth=True
                         )
    theBar.render()
    return theBar.render_embed()


if __name__ == "__main__":
    a = ReadCsv()
    t = a.loadcsv("result.csv")
    if t != -1:
        l1 = []
        l2 = []
        ll = []
        for i in range(len(t)):
            if i != 0:
                l1.append(t[i][0])
                ll.append(t[i][1])
        l2.append(ll)
        print(l1)
        print(l2)
        getBar(l1, l2)

