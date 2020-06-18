import pandas as pd
import csv

data1 = pd.read_csv("wash1.csv",)
data2 = pd.read_csv("wash2.csv",)

data1['发布时间'] = data1['发布时间'].str.split(' ', expand=True)[0]
data2['发布时间'] = data2['发布时间'].str.split(' ', expand=True)[0]

data1['发布时间'] = data1['发布时间'].str.split('-', expand=True)[1] + '/' + data1['发布时间'].str.split('-', expand=True)[2]
data2['发布时间'] = data2['发布时间'].str.split('-', expand=True)[1] + '/' + data2['发布时间'].str.split('-', expand=True)[2]

count = 1

result = []
temp = []

for row in data1.index:
    if data1.loc[row].values[1] == '04/01':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '04/02':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '04/03':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '04/04':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '04/05':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '04/06':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '04/07':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '04/08':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '04/09':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '04/10':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '04/11':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '04/12':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '04/13':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '04/14':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '04/15':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '04/16':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '04/17':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '04/18':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '04/19':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '04/20':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '04/21':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '04/22':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '04/23':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '04/24':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '04/25':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '04/26':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '04/27':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data2.index:
    if data2.loc[row].values[1] == '04/28':
        temp.append(data2.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '04/29':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

for row in data1.index:
    if data1.loc[row].values[1] == '04/30':
        temp.append(data1.loc[row].values)
        count = count + 1
    if count == 16:
        result = result + temp
        temp = []
        count = 1
        break

with open('TrumpFinal.csv', 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in result:
        writer.writerow(row)
