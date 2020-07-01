from flask import Flask ,jsonify,render_template,url_for,redirect,abort, request
from flask_sqlalchemy import *
from Visualization.picGenerate.picture import *

app = Flask('kkk')
@app.route('/hello', methods=['GET', 'POST'])
def test1():
    name = "特朗普"
    key = 'trump'
    m1 = weibo_m_emo(key)
    m = weibo_predict(key)
    m7 = weibo_bodong(key)
    c = wordcloud(key)
    kkk = weiboredian(key)
    return render_template("test.html",
                           name=name,
                           m2=m1[0],
                           m3=m1[1],
                           m4=m1[2],
                           m5=m1[3],
                           m6=m,
                           m7=m7,
                           c1=c[0],
                           c2=c[1],
                           c3=c[2],
                           kkk = kkk)


app.run()

