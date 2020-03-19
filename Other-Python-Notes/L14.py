# coding : utf-8

""" 类和对象训练 """
class Circle(object):
    pi = 3.14
    def __init__(self , r):  #创建类别漏了初始化
        self.rad = r
    def area(self):
        a = self.pi * self.rad**2 # **指平方
        return a
x = Circle(3)
print(x.area())

""" 模块导入训练 """
import hello as h
h.display()

""" 利用搜索路径来导入模块 """
import sys
print(sys.path) # python会从这些路径中去找文件
# import test1 # 因为test1不在这个当前路径下，所以找不到
sys.path.append("D:\learnCode\learnPython\model") # 将此路径加入sys的搜索范围中，可以直接写“model”，表示当前路径添加model
# print(sys.path)
import test1
test1.display()

""" 导入包的模块 """
import package.hello as h
h.hi()

""" 学习模块测试 """
import package.moduleTest as t
print(t.cal(1 , 2))
print(t.__name__) # 在主程序中调用 模块.name是模块的名字
print(__name__) # 而主程序的 name是main

""" 注意变量命名 """
a = (1 , 2 ,4)
a = list(a) # list函数可以将元组转成列表
print(a)
list = [1 , 2 , 3]
# b = list(a) # 如果已经拿list做变量名，则不能用list将元组转为列表

print(dir(list)) # dir可以列出所有属性和方法
print(help(list.sort)) # help可以给出具体的属性或方法的定义