import pandas as pd

data1 = pd.read_csv("trumpMarch.csv")
#data2 = pd.read_csv("Aprilplus.csv")

data1.drop(data1.columns[[0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16]], axis=1, inplace=True)
#data2.drop(data2.columns[[0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16]], axis=1, inplace=True)

df1 = pd.DataFrame(data1)
#df2 = pd.DataFrame(data2)

df1.to_csv('washMarch.csv', index=None)
#df2.to_csv('washAprilPlus.csv', index=None)
