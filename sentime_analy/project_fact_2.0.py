import csv
import re
import time

import pandas as pd
import requests
import json
import  numpy as np
App_Key = 'X2Is9l1CzRciITL1ujm8cBH7'#
Secret_Key = 'U47FKZaGwleFu20MNcPxaYSHyvsF3BEe'

import json
from  MyEncoder import  NpEncoder

# 情感分析

res_sent=[]
res_sent_www=[]
def last_getProEmotion(inputText, access_token): #情感分析的函数
    url = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify_custom?access_token=' + access_token
    header = {'Content-Type	': 'application/json'}
    body = {'text': inputText}
    requests.packages.urllib3.disable_warnings()
    res = requests.post(url=url, data=json.dumps(body, cls=NpEncoder), headers=header, verify=False)
    time.sleep(1)

    global  res_sent
    global  res_sent_www
    if res.status_code == 200:
        info = json.loads(res.text)
        print(info)
        if 'items' in info and len(info['items']) > 0:
            sentiment = info['items'][0]['sentiment']
            if(sentiment==0):
                res_sent_www.append(-2)
            else:
                res_sent_www.append(sentiment)
            res_sent.append(sentiment)
            # if(sentiment==0):
            #     res_sent_0change.append(-2)
            # else:
            # res_sent_0change.append(sentiment)

            print("ok")



# 获取token
def getToken():
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + App_Key + '&client_secret=' + Secret_Key
    response = requests.get(host)
    time.sleep(1)
    if response.status_code == 200:
        info = json.loads(response.text)  # 将字符串转成字典
        access_token = info['access_token']  # 解析数据到access_token
        return access_token
    return ''

def cut_text(text, lenth):
    textArr = re.findall('.{' + str(lenth) + '}', text)
    textArr.append(text[(len(textArr) * lenth):])
    return textArr[0]  # 返回多段值


# 主函数
def main():
    df=pd.read_csv('TrumpFebruaryFinal.csv',encoding='utf-8',usecols=[0])
    global res_sent
    global res_sent_www
    arr_result=[]#存放每天的均值，总共31个
    arr_ans=[]
    sys_out_list_withtime = [[[] for i in range(3)] for j in range(31)]
    for i in range(0, len(df)):   #文件行数，报错可以修改，应该没啥问题
            print(i)
            time.sleep(1)
            # inputText = df.loc[i].values[0:]
            inputText=df.at[i,"微博正文"]
            print(inputText)
            if(len(inputText)<2048):
               accessToken = getToken()
               last_getProEmotion(inputText,accessToken)
            else:
                data = cut_text(inputText, 1500)  # 如果文章字节长度大于1500，则切分
                accessToken = getToken()
                last_getProEmotion(data , accessToken)



    # print(res_sent_www)
    for i in range(0,31):
        sys_out_list_withtime[i][0]='5/'+(i+1).__str__()          #这个是调整时间的


    arr_result.append(np.mean(res_sent[0:15]))
    arr_ans.append(np.mean(res_sent_www[0:15]))
    sys_out_list_withtime[0][1]=arr_result[0]
    sys_out_list_withtime[0][2]=arr_ans[0]
    # print(arr_result[0])
    # print(arr_result_change[0])
    for i in range(1,31):
        end=np.int((i+1)*15)
        before=np.int(i*15)
        arr_result.append(np.mean(res_sent[before:end]))
        arr_ans.append(np.mean(res_sent_www[before:end]))
        sys_out_list_withtime[i][1]=arr_result[i]
        sys_out_list_withtime[i][2]=arr_ans[i]
    # print(arr_result_change)
    # print(arr_result)
    print(arr_ans)
    print("带时间",end=" ")
    print(sys_out_list_withtime)

#运行完复制结果到tencent，然后运行保存到csv文件，方便看结果

if __name__ == '__main__':
    main()
