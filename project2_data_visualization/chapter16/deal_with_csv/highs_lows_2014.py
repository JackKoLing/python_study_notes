# coding: utf-8

import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'project2_data_visualization\chapter16'
filename += '\deal_with_csv\sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader) # 获得一行信息，保存在列表中
    # print(header_row)

    """ 
    for index, column_header in enumerate(header_row):
        # enumerate(列表)可以对应每个元素的下标和值
        print(index, column_header)
    """

    # 从文件中获取日期和最高气温、最低温度
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        highs.append(int(row[1]))
        lows.append(int(row[3]))
    
# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5) # alpha为透明度
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形的格式
plt.title("Daily high and low temperatures - 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate() # 制作斜的标签，避免重叠
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16) # 刻度大小

plt.show()