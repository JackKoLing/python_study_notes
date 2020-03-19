# coding: utf-8

import pygal
from dice import Dice

# 创建一个D6
dice = Dice()

# 扔几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = dice.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, dice.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化(绘制直方图)
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies) # 标签、数值
# 保存为svg格式文件，方便浏览器打开
file_name = 'project2_data_visualization\\chapter15\\'
file_name += 'throw_dice_simulation\\dice_visual.svg'
hist.render_to_file(file_name)
