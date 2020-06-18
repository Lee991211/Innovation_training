import pandas as pd
import csv

data1 = pd.read_csv("washMarch.csv",)
# data2 = pd.read_csv("washAprilPlus.csv",)

data1['发布时间'] = data1['发布时间'].str.split(' ', expand=True)[0]
# data2['发布时间'] = data2['发布时间'].str.split(' ', expand=True)[0]

data1['发布时间'] = data1['发布时间'].str.split('-', expand=True)[1] + '/' + data1['发布时间'].str.split('-', expand=True)[2]
# data2['发布时间'] = data2['发布时间'].str.split('-', expand=True)[1] + '/' + data2['发布时间'].str.split('-', expand=True)[2]

count = 1

result = []
temp = []

for row in data1.index:
    if data1.loc[row].values[1] == '03/01':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '03/02':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '03/03':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '03/03':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '03/05':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '03/06':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '03/07':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '03/08':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '03/09':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '03/10':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '03/11':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '03/12':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '03/13':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '03/14':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '03/15':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '03/16':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '03/17':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '03/18':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '03/19':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '03/20':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '03/21':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '03/22':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '03/23':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '03/24':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '03/25':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '03/26':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '03/27':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '03/28':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '03/29':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '03/30':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '03/31':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

with open('TrumpMarchFinal.csv', 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in result:
        writer.writerow(row)
