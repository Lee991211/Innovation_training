import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
import pandas as pd
import os
from keras.models import Sequential, load_model
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

dataframe = pd.read_csv('./dataraw.csv', usecols=[2], engine='python', skipfooter=3)
dataset = dataframe.values
# 将整型变为float
dataset = dataset.astype('float32')
#归一化 在下一步会讲解
scaler = MinMaxScaler(feature_range=(0, 1))
dataset = scaler.fit_transform(dataset)

train_size = int(len(dataset) * 0.65)
trainlist = dataset[:train_size]
testlist = dataset[train_size:]


def create_dataset(dataset, timesteps=36,predict_size=6):#构造数据集
    datax=[]#构造x
    datay=[]#构造y
    for each in range(len(dataset)-timesteps - predict_steps):
        x = dataset[each:each+timesteps,0]
        y = dataset[each+timesteps:each+timesteps+predict_steps,0]
        datax.append(x)
        datay.append(y)
    return np.array(datax),np.array(datay)
timesteps = 9
predict_steps = 10
trainX,trainY  = create_dataset(trainlist,timesteps,predict_steps)
testX,testY = create_dataset(testlist,timesteps,predict_steps)

trainX = np.reshape(trainX, (trainX.shape[0], trainX.shape[1], 1))
testX = np.reshape(testX, (testX.shape[0], testX.shape[1] ,1 ))

# create and fit the LSTM network
model = Sequential()
model.add(LSTM(128,input_shape=(timesteps,1),return_sequences= True))
model.add(Dropout(0.5))
model.add(LSTM(128,return_sequences=True))
model.add(LSTM(64,return_sequences=False))
model.add(Dense(predict_steps))
model.compile(loss="mean_squared_error",optimizer="adam")
model.fit(trainX,trainY, epochs= 400, batch_size=10)
model.save(os.path.join("DATA","Test" + ".h5"))
# make predictions


predict_xlist = []
predict_y = []#添加预测y列表
predict_xlist.extend(dataset[dataset.shape[0]-timesteps:dataset.shape[0],0].tolist())
while len(predict_y) < 30:
    predictx = np.array(predict_xlist[-timesteps:])#从最新的predict_xlist取出timesteps个数据，预测新的predict_steps个数据（因为每次预测的y会添加到predict_xlist列表中，为了预测将来的值，所以每次构造的x要取这个列表中最后的timesteps个数据词啊性）
    predictx = np.reshape(predictx,(1,timesteps,1))#变换格式，适应LSTM模型
    lstm_predict = model.predict(predictx)
    predict_xlist.extend(lstm_predict[0])#将新预测出来的predict_steps个数据，加入predict_xlist列表，用于下次预测
    # invert
    lstm_predict = scaler.inverse_transform(lstm_predict)
    predict_y.extend(lstm_predict[0])
l = predict_y
y_ture = np.array(dataset[-30:])
train_score = np.sqrt(mean_squared_error(y_ture,predict_y))
print("train score RMSE: %.2f"% train_score)
dataframe1 = pd.read_csv('dataraw.csv', usecols=[0])
dfd = dataframe1.values
topic = []
date = dfd[-1][0]
date1 = []
pre = []
pla = []
tes = []
testPredict = predict_y
for jk in range(0,len(testPredict)):
    tes.append(testPredict[jk])
    date1.append( str( jk + 1))
    topic.append('trump')
    pre.append('1')
    pla.append('1')
data = {
    'ds':date1,
    'emotion_val':tes,
    'topic':topic,
    'predict':pre,
    'platform':pla

}
df = pd.DataFrame(data)
df.to_csv('Result.csv',index=False)
plt.plot(l)
plt.plot(y_ture)
plt.show()
