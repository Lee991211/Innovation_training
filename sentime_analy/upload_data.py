import pandas as pd
import  numpy as np
df = pd.read_csv('zns.csv', encoding='utf-8', usecols=[1])
# print(df)检查是否正确
dat_list=[]
lol_list=[1.7333333333333334,1.7333333333333334, 1.4666666666666666, 1.6666666666666667, 1.4666666666666666, 1.9333333333333333, 2.0, 1.6666666666666667, 1.7333333333333334, 1.4666666666666666, 1.8666666666666667, 1.7333333333333334, 1.6666666666666667, 1.7333333333333334, 1.7333333333333334, 1.7333333333333334, 1.7333333333333334, 1.7333333333333334, 1.4666666666666666, 2.0, 1.7333333333333334, 1.7333333333333334, 1.4, 1.7333333333333334, 1.7333333333333334, 1.7333333333333334, 1.4666666666666666, 1.6666666666666667, 2.0, 1.4666666666666666, 1.4666666666666666, 1.4, 1.6666666666666667, 2.0, 1.2, 1.1333333333333333, 2.0, 2.0, 1.4, 1.7333333333333334, 1.4666666666666666, 0.6, 2.0, 1.4, 2.0, 1.9333333333333333, 1.6666666666666667, 1.8666666666666667, 2.0, 1.6666666666666667, 1.9333333333333333, 1.4666666666666666, 2.0, 1.6, 1.7333333333333334, 1.4666666666666666, 2.0, 1.4666666666666666, 2.0, 1.6666666666666667, 0.9333333333333333, 1.6666666666666667, 1.7333333333333334, 1.7333333333333334, 0.9333333333333333, 1.7333333333333334, 1.4, 1.6666666666666667, 1.9333333333333333, 1.7333333333333334, 2.0, 1.6666666666666667, 1.7333333333333334, 2.0, 1.2, 1.4666666666666666, 2.0, 1.7333333333333334, 2.0, 1.4666666666666666, 1.2, 0.9333333333333333, 1.4666666666666666, 1.4666666666666666, 1.6, 0.6666666666666666, 0.8, 2.0, 1.9333333333333333, 1.7333333333333334, 2.0, 1.6666666666666667, 1.7333333333333334, 1.2, 1.7333333333333334, 1.2, 1.7333333333333334, 1.2, 1.8666666666666667, 1.6666666666666667, 1.2, 1.2, 2.0, 1.8666666666666667, 2.0, 1.2, 1.1333333333333333, 1.6666666666666667, 1.2, 1.4666666666666666, 2.0, 1.2, 1.2, 1.4, 1.9333333333333333, 1.4, 0.6, 1.4666666666666666, 1.7333333333333334, 1.4, 1.7333333333333334]
zns_list=[1.6666666666666667,1.6666666666666667, 0.06666666666666667, 1.6666666666666667, 1.4, 0.9333333333333333, 0.6, 2.0, 1.4666666666666666, 1.2, 0.9333333333333333, 1.4, 1.2, 1.7333333333333334, 1.4666666666666666, 2.0, 1.4, 1.4666666666666666, 1.9333333333333333, 1.7333333333333334, 2.0, 1.0666666666666667, 1.7333333333333334, 1.4, 1.4, 1.6666666666666667, 1.0666666666666667, 1.6666666666666667, 2.0, 1.6666666666666667, 2.0, 1.4666666666666666, 1.7333333333333334, 1.7333333333333334, 1.7333333333333334, 1.9333333333333333, 1.6, 1.2, 1.4666666666666666, 1.9333333333333333, 1.7333333333333334, 1.6, 1.7333333333333334, 1.0666666666666667, 1.4, 1.4, 1.4, 0.6, 1.6666666666666667, 2.0, 1.2, 1.1333333333333333, 1.3333333333333333, 1.4666666666666666, 2.0, 1.7333333333333334, 0.8666666666666667, 2.0, 1.2666666666666666, 1.4666666666666666, 1.4666666666666666, 1.3333333333333333, 1.4666666666666666, 2.0, 1.7333333333333334, 2.0, 0.6666666666666666, 1.7333333333333334, 1.4666666666666666, 1.7333333333333334, 1.4, 1.4666666666666666, 1.7333333333333334, 1.7333333333333334, 0.6666666666666666, 0.5333333333333333, 2.0, 1.2, 1.4, 1.2, 2.0, 1.7333333333333334, 1.4666666666666666, 1.6666666666666667, 1.4, 1.4666666666666666, 2.0, 1.7333333333333334, 2.0, 1.4, 1.4, 2.0, 1.4666666666666666, 2.0, 2.0, 1.9333333333333333, 1.0666666666666667, 1.7333333333333334, 0.8, 1.7333333333333334, 0.6666666666666666, 2.0, 1.2, 0.6666666666666666, 2.0, 1.3333333333333333, 1.4666666666666666, 1.1333333333333333, 1.2, 1.6666666666666667, 0.8, 2.0, 1.8666666666666667, 1.4666666666666666, 1.4666666666666666, 2.0, 1.4666666666666666, 1.6666666666666667, 1.4666666666666666, 2.0, 2.0]
top_list=[]
top_list1=[]
pre_list=[]
for i in  range(0,len(df),15):
   index=df.at[i,"日期"]
   # print(index)
   dat_list.append(index)
   pre_list.append(0)
   top_list.append('zns')
   top_list1.append('lol')


datta={
    'ds': dat_list,
    'emotion_val':zns_list,
    'topic': top_list,
    'predict': pre_list,
}
datta1={
    'ds': dat_list,
    'emotion_val': lol_list,
    'topic': top_list1,
    'predict': pre_list
}
# print(len(datta['ds']))
# print(len(datta['emotion_val']))
# print(len(datta['topic']))
# print(len(datta['predict'])) #检查行数
# print(len(lol_list))
df = pd.DataFrame(datta)
df.to_csv('zns_rrreal.csv',index=False)
df1=pd.DataFrame(datta1)
df1.to_csv('lol_rrreal.csv',index=False)
