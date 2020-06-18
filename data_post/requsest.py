import requests, json
import csv
#上传爬虫爬取数据的方法
#单元格格式为ds，context，topic，分别为时间、文本、话题
#李哲荀用
def insert_rawdata(filepath,url):
    data_dict = {"data": []}
    data_list = []
    with open(filepath, 'r', encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        fieldnames = next(reader)  # 获取数据的第一列，作为后续要转为字典的键名 生成器，next方法获取
        # print(fieldnames)
        csv_reader = csv.DictReader(f,fieldnames=fieldnames)  # self._fieldnames = fieldnames   # list of keys for the dict 以list的形式存放键名
        for row in csv_reader:
            d = {}
            for k, v in row.items():
                d[k] = v
            data_dict["data"].append(d)
            # print(d)
    raw_data = json.dumps(data_dict)

    print(raw_data)
    r = requests.post(url, raw_data)


##上传原始数据经过二次处理后数据和最终预测结果的方法
#单元格格式为ds，emotion_val，topic，predict分别代表时间、话题情感值、话题、该行数据是否为预测值
# predict只有0、1两个属性，0代表这行数据不是预测得到的，1代表这行数据是预测得到的
#杨涛、杨秀辉用
def insert_emotionval(filepath,url):
    data_dict = {"data": []}
    data_list = []
    with open(filepath, 'r', encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        fieldnames = next(reader)  # 获取数据的第一列，作为后续要转为字典的键名 生成器，next方法获取
        # print(fieldnames)
        csv_reader = csv.DictReader(f,fieldnames=fieldnames)  # self._fieldnames = fieldnames   # list of keys for the dict 以list的形式存放键名
        for row in csv_reader:
            d = {}
            for k, v in row.items():
                d[k] = v
            data_dict["data"].append(d)
            # print(d)
    raw_data = json.dumps(data_dict)

    print(raw_data)
    r = requests.post(url, raw_data)

insert_rawdata(r'C:\Users\Lee\PycharmProjects\inno_train\data_post\rawdata.csv','http://127.0.0.1:5000/insert_rawdata')
insert_emotionval(r'C:\Users\Lee\PycharmProjects\inno_train\data_post\midddata.csv','http://127.0.0.1:5000/insert_emotionval')
