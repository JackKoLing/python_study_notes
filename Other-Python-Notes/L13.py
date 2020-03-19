# coding : utf-8
""" 学习模块(module)概念,模块就是把功能放在一起，写成一段程序，提供其他程序调用 """
""" 导入模块 """
# import calendar # 导入日历模块
# print(calendar) # 显示模块文件所在位置 
# cal = calendar.month(2020 , 1)
# print(cal)

# import hello as h # 导入的模块需要在同一个路径下才找得到
# h.hi()

# from hello import name # 指定模块的某个函数
# name("Jackko")
# from hello import * # 导入该模块所有函数，但是不建议
# name("ss")

# """ 学习输入input """
# print("he")
# num = int(input("请输入一个数字：")) # 注意输入的都是字符串类型，要换类型需要强制转换
# print(type(num))

""" 写一个猜数字程序 """
import random
num = random.randint(1 , 10) # 生成一个从1到10的随机整数，包括10
print("我正在想一个1到10之间的整数")
for i in range(1 , 7):
    print("猜猜看，这个数字是：")
    guess = int(input())
    if num > guess:
        print("太小啦")
    elif num < guess:
        print("太大啦")
    else:
        print("恭喜你，猜对啦！你一共猜了" + str(i) + "次")
        break
print("游戏结束")