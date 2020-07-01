# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 15:02
# @Author  : 尹成林
# @Site    : https://me.csdn.net/sdyinruichao
# @File    : readDbs.py
# @Software: PyCharm
import pyecharts.options as opts
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType


def Getpie():
    pie = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC))
            .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
            .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )

    pie.render('pie.html')