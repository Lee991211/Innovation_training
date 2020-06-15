# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 9:00
# @Author  : 尹成林
# @Site    : https://me.csdn.net/sdyinruichao
# @File    : read_file.py
# @Software: PyCharm

from pyecharts.charts import Line
import pyecharts.options as opts
from pyecharts.faker import Faker

testdata = [[0.35906672], [0.28135723], [0.40640217],
 [0.35906672],
 [0.35906672],
 [0.28135723],
 [0.40640217],
 [0.35906672],
 [0.35906672],
 [0.28135723],
 [0.40640217],
 [0.35906672],
 [0.35906672],
 [0.28135723],
 [0.40640217],
 [0.35906672],
 [0.35906672],
 [0.28135723],
 [0.40640217],
 [0.35906672],
 [0.35906672],
 [0.28135723],
 [0.40640217],
 [0.35906672],
 [0.35906672],
 [0.28135723],
 [0.40640217],
 [0.35906672],
 [0.35906672],
 [0.28135723]]

usingdata = []
for i in testdata:
    usingdata.append(round(i[0], 2))

days = []
for i in range(30):
    days.append(i+1)

line1=(
    Line() # 生成line类型图表
    .add_xaxis(days)
    .add_yaxis('预测指数', usingdata, markline_opts=opts.MarkLineOpts(
            data=[
                opts.MarkLineItem(type_="average", name="平均值"),
                opts.MarkLineItem(symbol="none", x="90%", y="max"),
                opts.MarkLineItem(symbol="circle", type_="max", name="最高点"),
            ]
        ),is_smooth=True)


    # .add_yaxis('数据2',Faker.values())
    .set_global_opts(title_opts=opts.TitleOpts(title='某事件30天预测demo'),

                     tooltip_opts=opts.TooltipOpts(trigger="axis"),
                     toolbox_opts=opts.ToolboxOpts(is_show=True),
                     # toolbox_opts=opts.ToolboxOpts("bar"),
                     xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
                     )
)
line1.render('pyecharts-line.html')
print(Faker.values())
print(testdata[0][0])

