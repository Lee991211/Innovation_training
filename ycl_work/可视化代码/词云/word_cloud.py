# -*- coding: utf-8 -*-
# @Time    : 2020/6/7 16:01
# @Author  : 尹成林
# @Site    : https://me.csdn.net/sdyinruichao
# @File    : word_cloud.py
# @Software: PyCharm

import jieba
import jieba.analyse
import re
from pyecharts.charts import WordCloud
import pyecharts.options as opts

sourceTxt = 'data/test.txt'
source1Txt = 'data/test1.txt'
targetTxt = 'data/target.txt'

jieba.analyse.set_stop_words('data/baidu_stopwords.txt')


# 去除掉汉字
def find_unchinese(file):
    pattern = re.compile(r'[\u4e00-\u9fa5]')
    unchinese = re.sub(pattern, "", file)
    print(unchinese)

with open(sourceTxt, 'r', encoding = 'utf-8') as sourceFile, open(source1Txt, 'a+', encoding = 'utf-8') as targetFile:
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    for line in sourceFile:
        # seg = jieba.cut(line.strip(), cut_all = False)
        # 分好词之后之间用空格隔断
        output = re.sub(pattern, "",  line)
        targetFile.write(output)
        targetFile.write('\n')


words = []  # 可以存储生成词云的数据


# 对文本进行操作
with open(source1Txt, 'r', encoding = 'utf-8') as sourceFile, open(targetTxt, 'a+', encoding = 'utf-8') as targetFile:
    for line in sourceFile:
        seg = jieba.cut(line.strip(), cut_all = False)
        # 分好词之后之间用空格隔断
        output = ' '.join(seg)
        targetFile.write(output)
        targetFile.write('\n')
    print('ycl写入成功！')

keywords = []

with open(targetTxt, 'r', encoding = 'utf-8') as file:
    text = file.readlines()
    """
    几个参数解释：
        * text : 待提取的字符串类型文本
        * topK : 返回TF-IDF权重最大的关键词的个数，默认为20个
        * withWeight : 是否返回关键词的权重值，默认为False
        * allowPOS : 包含指定词性的词，默认为空
    """
    keywords = jieba.analyse.extract_tags(str(text), topK = 30, withWeight=True, allowPOS=())
    print(keywords)
    for i in keywords:
        a = i[0]
        b = float(i[1])*100
        words.append((a, b))
    print(words)


(
    WordCloud()
    .add(series_name="ycl热点分析", data_pair=keywords, word_size_range=[20, 80])
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="热点分析", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
    .render("basic_wordcloud.html")
)

