# coding: utf-8

import pygal
from dice import Dice

# 创建两个D6骰子
dice_1 = Dice()
dice_2 = Dice()

# 扔几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = dice_1.roll() + dice_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = dice_1.num_sides + dice_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化(绘制直方图)
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies) # 标签、数值
# 保存为svg格式文件，方便浏览器打开
file_name = 'project2_data_visualization\\chapter15\\'
file_name += 'throw_dice_simulation\\two_dices_visual.svg'
hist.render_to_file(file_name)