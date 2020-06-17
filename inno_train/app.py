import string
from flask import request
from flask import Flask, jsonify, render_template
from jieba.analyse import extract_tags
import utils
import decimal


import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://test:123456@47.98.141.4:3306/innotrain?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class rawdata(db.Model):
    __tablename__ = 'raw_data'
    id = db.Column(db.Integer,primary_key=True)
    context = db.Column(db.String())
    ds = db.Column(db.String())
    # ds = db.Column(db.Date())
    topic = db.Column(db.String())
    def __init__(self, context, ds,topic):
        self.ds = ds
        self.topic = topic
        self.context = context
        # self.id = id

    def __repr__(self):
        return '<rawdata:%s %s %s %s>' % (self.id,self.context,self.ds,self.topic)
class emotion_val(db.Model):
    __tablename__ = 'emotion_val'
    id = db.Column(db.Integer,primary_key=True)
    predict= db.Column(db.Integer())
    emotion_val = db.Column(db.String())
    ds = db.Column(db.String())
    # ds = db.Column(db.Date())
    topic = db.Column(db.String())
    def __init__(self, emotion_val, ds,topic,predict):
        self.emotion_val = emotion_val
        self.predict = predict
        self.ds = ds
        self.topic = topic

    def __repr__(self):
        return '<rawdata:%s %s %s %s>' % (self.emotion_val,self.ds,self.topic,self.predict)

@app.route('/')
def hello_world():
    return render_template("pyecharts-line.html")

#获取预测数据的接口
@app.route('/get_predict')
def get_predict():
    data = utils.get_predict()
    ds=[]
    emotion_val=[]
    topic = []
    for each in data:
        ds.append(each[0])
        emotion_val.append(each[1])
        topic.append(each[2])

    return jsonify({"ds":ds,"emotion_val":emotion_val,"topic":topic})

#获取预测数据和二次处理后真实数据两者的接口
@app.route('/get_emotionval')
def get_emotionval():
    data = utils.get_emotion_val()
    ds=[]
    emotion_val=[]
    topic = []
    predict = []
    for each in data:
        ds.append(each[0])
        emotion_val.append(each[1])
        topic.append(each[2])
        predict.append(each[3])
    return jsonify({"ds":ds,"emotion_val":emotion_val,"topic":topic,"predict":predict})

#获取爬虫爬取数据数据的接口，杨涛用
@app.route('/get_rawdata')
def get_rawdata():
    data = utils.get_rawdata()
    ds = []
    id = []
    context=[]
    topic=[]
    for each in data:
        print(each)
        ds.append(each[1])
        context.append(each[0])
        topic.append(each[2])
    return jsonify({"ds":ds,"context":context,"topic":topic})


#获取二次处理后真实数据的接口，杨秀辉用
@app.route('/get_midrawdata')
def get_midrawdata():
    data = utils.get_midrawdata()
    ds = []
    emotion_val=[]
    topic=[]
    for each in data:
        ds.append(each[0])
        emotion_val.append(each[1])
        topic.append(each[2])
    return jsonify({"ds":ds,"emotion_val":emotion_val,"topic":topic})


#上传爬虫爬取数据的接口，李哲荀用
@app.route('/insert_rawdata',methods = ['GET','POST'])
def insert_rawdata():
    if not request.data:
        return ('no data!')
    print("This is a "+request.method+" method!")
    #先将收到json数据的编码格式从bytes改成utf-8
    rawdata_json = request.data.decode('utf-8')
    print(rawdata_json)
    #json.loads()将json格式的数据解码为python的dict格式数据
    #json.dumps()将python的dict格式的数据编码为json格式数据
    rawdata_dict = json.loads(rawdata_json)
    print(type(rawdata_dict))
    for raw in rawdata_dict['data']:
        # print(raw)
        db.session.add(rawdata( context=raw['context'], ds=raw['ds'], topic=raw['topic']))
    db.session.commit()
    return "ok"


#上传二次处理数据和预测得到数据的接口，杨涛，杨秀辉用
@app.route('/insert_emotionval',methods = ['GET','POST'])
def insert_emotionval():
    if not request.data:
        return ('no data!')
    print("This is a "+request.method+" method!")
    #先将收到json数据的编码格式从bytes改成utf-8
    emoval_json = request.data.decode('utf-8')
    print(emoval_json)
    #json.loads()将json格式的数据解码为python的dict格式数据
    #json.dumps()将python的dict格式的数据编码为json格式数据
    emoval_dict = json.loads(emoval_json)
    print(type(emoval_dict))
    # print ((rawdata_dict['ds']))
    # print(ds)
    # rawdata=request.data
    for raw in emoval_dict['data']:
        # print(raw)
        db.session.add(emotion_val( emotion_val=raw['emotion_val'], ds=raw['ds'], topic=raw['topic'], predict=raw['predict']))
    db.session.commit()
    return "ok"





@app.route("/time")
def get_time():
    return utils.get_time()


if __name__ == '__main__':
    app.run()
