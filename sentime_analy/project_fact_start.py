import csv

import pandas as pd
import requests
import json
#
App_Key = 'X2Is9l1CzRciITL1ujm8cBH7'
Secret_Key = 'U47FKZaGwleFu20MNcPxaYSHyvsF3BEe'

import json
from  MyEncoder import  NpEncoder

# 情感分析
def getEmotion(inputText, access_token):
    url = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify_custom?access_token=' + access_token
    header = {'Content-Type	': 'application/json'}
    body = {'text': inputText}
    requests.packages.urllib3.disable_warnings()
    res = requests.post(url=url, data=json.dumps(body,cls=NpEncoder), headers=header, verify=False)


    if res.status_code == 200:
        info = json.loads(res.text)
       # print(info)
        if 'items' in info and len(info['items']) > 0:
            sentiment = info['items'][0]['sentiment']
            if sentiment == 2:
                # print(inputText + '  情感分析结果是:正向')
                return 2
            elif sentiment == 1:
                # print(inputText + '  情感分析结果是:中性')
                return  1
            else:
                # print(inputText + '  情感分析结果是:负向')
                 return  0


# 获取token
def getToken():
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + App_Key + '&client_secret=' + Secret_Key
    response = requests.get(host)

    if response.status_code == 200:
        info = json.loads(response.text)  # 将字符串转成字典
        access_token = info['access_token']  # 解析数据到access_token
        return access_token
    return ''

pos_num=0
nev_num=0
med_num=0
cont=0

# 主函数
def main():

    df= pd.read_csv('data.csv',encoding='utf-8',usecols=[4])#读取文件，可替换文件
    sys_out_list=[[[] for i in range(3)] for j in range(50)] #最后展示的输出，这个是50行，3列，每行的数据是正向，重型，负面，可以根据读入的数据改
    global cont, pos_num, med_num, nev_num
    for i in range(1,500):
            print(i)
            inputText = df.loc[i].values[0:]
            accessToken = getToken()
            if(getEmotion(inputText, accessToken)==2): #这个是正向
                pos_num=pos_num+1
            elif (getEmotion(inputText, accessToken) == 1):# 这个是中性
                med_num = med_num + 1
            else:
                nev_num = nev_num + 1             #这个是负向

            if ((i% 10 ==0 and i!=0) or i==df.shape[0]-1):# 我这里是10个为一组，为了快速测试，可以改，我想的是1000条，但是会慢点。
                sys_out_list[cont][0]=pos_num
                sys_out_list[cont][1]=med_num
                sys_out_list[cont][2]=nev_num
                cont=cont+1
                pos_num=nev_num=med_num=0
                print(sys_out_list)     #这个是最后的输出，每组看结果放这里，放前面可以等全部运行完




if __name__ == '__main__':
    main()
