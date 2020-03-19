# coding: utf-8

""" 第2章：变量和简单数据类型 """

# 2.2 变量
message = "Hello Python world！"
print(message)

message = "Hello Python Crash Course world!"
print(message)

# 2.3 字符串
# 修改字符串的大小写
name = "ada lovelace"
print(name.title()) # 每个单词的首字母变大写
print(name.upper()) # 每个单词变大写
print(name.lower()) # 每个单词变小写 

# 合并（拼接）字符串
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
message = "Hello," + full_name.title() + "!"
print(message) 

# 使用制表符\t和换行符\n来添加空白
print("\tpython")
print("Languages:\n\tPython\n\tC\t\nJavaScript")

# 删除空白
favorite_language = '  python   '
print(favorite_language.rstrip()) # 去除右边的空格
print(favorite_language.lstrip()) # 去除左边的空格
print(favorite_language.strip()) # 去除两边的空格 

# 使用str()
age = 24
message = "Happy " + str(age) + "rd Birthday!"
print(message)

# 2.4 数字
# python3的除法是保留小数点,python2是整数/整数=整数
print( 3/2 ) 

# 2.6 python之禅
import this 