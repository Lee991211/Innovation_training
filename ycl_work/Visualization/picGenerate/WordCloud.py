# -*- coding: utf-8 -*-
# @Time    : 2020/6/22 14:54
# @Author  : 尹成林
# @Site    : https://me.csdn.net/sdyinruichao
# @File    : WordCloud.py
# @Software: PyCharm

import sys
import jieba
import jieba.analyse
import re
from pyecharts.charts import WordCloud
import pyecharts.options as opts
from pyecharts.globals import ThemeType
sys.path.append("..")


# keywords = [( , ), ……, ( , )]
# name 为输入的名字
def getWordCloud(keywords, name, T = 0):
    WC = (
        WordCloud(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC))
            .add(series_name="{}词云图".format(name), data_pair=keywords, word_size_range=[40, 120])
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="{}词云图".format(name), title_textstyle_opts=opts.TextStyleOpts(font_size=30)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
    )
    WC.render()
    return WC.render_embed()


if __name__ == "__main__":
    a = [('特朗普', 78.74096463001472), ('美国', 16.71608097087396), ('总统', 6.817801148287151), ('风景线', 6.8127394056179496), ('中国', 6.532717519030898), ('白宫', 5.029245554100294), ('疫情', 4.362531550841099), ('世界', 3.641392834462482), ('病毒', 3.63784713120157), ('美丽', 3.5818577330370283), ('川普', 3.5178325167925455), ('老特', 3.5178325167925455), ('加油', 2.8075050727123596), ('黑人', 2.6912479220868075), ('糟糕', 2.6562121365063756), ('不靠', 2.5183821497206966), ('骚乱', 2.4604486451069154), ('人民', 2.299375571504169), ('祈祷', 2.233522428858754), ('国家', 2.158160829512506), ('军队', 2.0967592171493377), ('建国', 2.056507498502452), ('低等', 1.819657643686121), ('大笑', 1.8090032726410004), ('赞赞', 1.7589162583962727), ('捂脸', 1.7589162583962727), ('甩锅', 1.7589162583962727), ('示威', 1.7547524461736144), ('希望', 1.6593770862515937), ('一个', 1.6581957658440412)]
    getWordCloud(a, "特朗普")

