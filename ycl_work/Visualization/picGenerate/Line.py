# -*- coding: utf-8 -*-
# @Time    : 2020/6/20 15:02
# @Author  : 尹成林
# @Site    : https://me.csdn.net/sdyinruichao
# @File    : readDbs.py
# @Software: PyCharm
import sys
import numpy as np
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.globals import ThemeType
sys.path.append("..")
from Visualization.dataProsc.readDbs import *


def GetLine(dataX, dataY, n=[0], T=0):
    chinaLine = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC))
        .add_xaxis(dataX)

        .set_global_opts(
            title_opts=opts.TitleOpts(title=""),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
        )
    )
    for i in range(len(dataY)):
        chinaLine.add_yaxis('{}月情感变化'.format(n[i]), dataY[i], is_symbol_show=True, label_opts=opts.LabelOpts(is_show=True),
                            markline_opts=opts.MarkLineOpts(
                                data=[
                                    opts.MarkLineItem(type_="average", name="平均值"),
                                    opts.MarkLineItem(symbol="none", x="90%", y="max"),
                                    opts.MarkLineItem(symbol="circle", type_="max", name="最高点"),
                                ]
                            ),
                        markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"), ]), is_smooth=True)
    # return chinaLine.render_embed()
    chinaLine.render()


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
        GetLine(l1, l2)
    # GetLine([0, 1, 2, 3, 4], [[2, 1, 5, 2, 6]])
