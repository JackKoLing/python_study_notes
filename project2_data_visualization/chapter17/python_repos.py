# coding: utf-8

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code) # 200表示请求成功

# 将API响应存储在一个变量中
response_dict = r.json() # 将获取的JSON格式的的信息转成字典
print("Total repositories:", response_dict['total_count'])

# 搜索有关仓库的信息
repo_dicts = response_dict['items']
# print("Repositories returned:", len(repo_dicts))

# print("\nKeys:", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),
        'xlink': repo_dict['html_url'],
        }
    plot_dicts.append(plot_dict)

# 可视化
my_style = LS('#333366', base_style=LCS)

# 创建配置对象，将参数传给Bar()
my_config = pygal.Config()
my_config.x_label_rotation = 45 # 标签绕x轴旋转45度
my_config.show_legend = False # 隐藏图标
my_config.title_font_size = 24
# my_config.label_font_size = 14 # 副标签大小
# my_config.major_label_font_size = 18 # 主标签（5000整数倍）大小
my_config.truncate_label = 10 # 较长项目名缩短为10个字符
my_config.show_y_guides = False # 隐藏水平线
# my_config.width = 100

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add(' ', plot_dicts)
chart.render_to_file('project2_data_visualization\chapter17\python_repos.svg')