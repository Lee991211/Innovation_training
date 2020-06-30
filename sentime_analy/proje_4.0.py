import csv
import re
import time

import pandas as pd
import requests
import json
import  numpy as np
App_Key = 'X2Is9l1CzRciITL1ujm8cBH7'#这两个是百度云的ak和sk
Secret_Key = 'U47FKZaGwleFu20MNcPxaYSHyvsF3BEe'

import json

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)


def getEmotion():

  everyday_list = []#存放全部的情感判断值
  mea_everday_list = []#存放平均后的判断值，每天取15个的平均值
  df = pd.read_csv('zns.csv', encoding='utf-8', usecols=[0])
  def last_getProEmotion(inputText, access_token): #情感分析的函数
      url = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify_custom?access_token=' + access_token
      header = {'Content-Type	': 'application/json'}
      body = {'text': inputText}
      requests.packages.urllib3.disable_warnings()
      res = requests.post(url=url, data=json.dumps(body, cls=NpEncoder), headers=header, verify=False)
      time.sleep(1)#因为qps限制是2，防止访问次数过多报错
      if res.status_code == 200:
        info = json.loads(res.text)
        print(info)
        if 'items' in info and len(info['items']) > 0:
            sentiment = info['items'][0]['sentiment'] #取出情感的判断
            if(sentiment==0):#2 1 0是原本返回结果，这样削弱了负面情感的占比，故而改成2 0 -2让正面和负面保持同等占比
                return -2
            else:
                return  sentiment

  def getToken():#token函数
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
      host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + App_Key + '&client_secret=' + Secret_Key
      response = requests.get(host)
      time.sleep(1)
      if response.status_code == 200:
          info = json.loads(response.text)  # 将字符串转成字典
          access_token = info['access_token']  # 解析数据到access_token
          return access_token
      return ''

  def cut_text(text, lenth):  #防止文本过长的报错，取1500个字段
      textArr = re.findall('.{' + str(lenth) + '}', text)
      textArr.append(text[(len(textArr) * lenth):])
      return textArr[0]  # 返回多段值





  for i in range(0,len(df)):
        print(i)
        time.sleep(1)
        inputText=df.at[i,"微博正文"]
        print(inputText)
        if(len(inputText)<2048):
            accessToken = getToken()
            everyday_list.append(last_getProEmotion(inputText,accessToken))
        else:
            data = cut_text(inputText, 1500)  # 如果文章字节长度大于1500，则切分
            accessToken = getToken()
            everyday_list.append(last_getProEmotion(data , accessToken))
  print(everyday_list)
  for  i in range(0,121):
        end=np.int((i+1)*15)
        before=np.int(i*15)
        mea_everday_list.append(np.mean(everyday_list[before:end]))
  # print(mea_everday_list)
  # print(everyday_list)
  return  mea_everday_list

print(getEmotion())
