# -*- coding: utf-8 -*-
# @Time    : 2020/6/10 13:21
# @Author  : 尹成林
# @Site    : https://me.csdn.net/sdyinruichao
# @File    : word_cloud.py
# @Software: PyCharm

from flask import Flask ,jsonify,render_template,url_for,redirect,abort, request
from flask_sqlalchemy import *
from wordcloud.word_cloud import make_wordcloud

app = Flask('kkk')
@app.route('/search', methods=['GET', 'POST'])
def test1():
    name = request.form.get('email1')
    if name == None:
        return render_template("index.html")
    else:
        # 这里调用爬虫
        return render_template("demo.html")


@app.route('/wordcloud', methods=['GET', 'POST'], endpoint="/worldcloud")
def test1():
    name = request.form.get('email1')
    a = make_wordcloud()
    return a


app.run()

