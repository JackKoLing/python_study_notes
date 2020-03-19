# coding: utf-8

""" 第10章：文件和异常 """

# 10.1 从文件中读取数据

import os
print(os.getcwd()) # vscode的主目录是以.vscode文件的所在目录为主目录

# 读取整个文件，使用with不用手动close()
with open(r'chapter10\pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# 逐行读取
filename = r'D:\learnCode\pythonBook\chapter10\pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# 将文件内容放在with程序块外处理
with open(filename) as file_object:
    lines = file_object.readlines() # 读出所有行，放在列表中
    print(lines)

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# 10.2 写入文件
# 写入空文件,如果文件不存在，则自动创建
filename = r'D:\learnCode\pythonBook\chapter10\pi_digits.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# 附加内容到文件
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

# 10.3 异常
# 处理ZeroDivisionError异常
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# 使用异常避免崩溃,使用try-except-else结构
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)

# 处理FileNotFoundError异常
def count_words(filename):
    """ 计算一个文件大致包含多少个单词 """
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print("Sorry, the file " + filename + " does not exist.")
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + 
            str(num_words) + " words.")

filename = r'D:\learnCode\pythonBook\chapter10\alice.txt'
count_words(filename)

# 失败时一声不吭
try:
    print(5/0)
except ZeroDivisionError:
    pass
print("done.")

# 10.4 存储数据
# 使用json.dump()将数据存到json文件
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = r'D:\learnCode\pythonBook\chapter10\numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj) # 一个参数是要存储的数据，一个是保存的文件对象

# 使用json.load()将数据读取到内存中
with open(filename) as f_obj:
    numbers = json.load(f_obj) # 只有文件对象这个参数
print(numbers)

# 保存和读取用户生成的数据
import json

username = input("What is your name? ")

filename = r'D:\learnCode\pythonBook\chapter10\username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")

# 重构：将代码划分为一系列完成具体工作的函数
import json

def get_stored_username():
    """ 如果存储了用户名，就获取它 """
    filename = r'D:\learnCode\pythonBook\chapter10\username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """ 提示用户输入用户名 """
    username = input("What is your name? ")
    filename = r'D:\learnCode\pythonBook\chapter10\username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """ 问候用户，并指出其名字 """
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")      
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()