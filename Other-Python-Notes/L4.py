# coding: utf-8
'''
学习python中list的创建、读取、修改、添加append（）、删除remove（）
'''
num = [1 , 2 , 3 , 4 , 5]
print(num)
weather = ["snow" , "rain" , "wind" , "cloud" , "sunny"]
print(weather)
color = ["red" , "green" , "blue"]
message = "My favourite color is " + color[0] + "."
print(message)
num[0] = "a"
print(num)

appearance = ["old" , "young" , "tall" , "short" , 'thin']
print(appearance)
appearance[3] = "fit"
print(appearance)

family = ["mom" , "dad" , "me" , "beibei"]
print(family)
family.append("miaomiao")
print(family)

fruniture = ["door" , "window" , "table" , "chair"]
print(fruniture)
fruniture.append("bed")
print(fruniture)

chocolate = ["coconut" , "almond" , "original" , "coffee"]
print(chocolate)
chocolate.remove("coconut")
chocolate.remove("almond")
chocolate.remove("original")
chocolate.remove("coffee")
print(chocolate)

animals = ["tiger" , "lion" , "monkey" , "deer"]
print(animals)
animals.remove("tiger")
print(animals)

a = [10 , 9 , 8 ,7]
print(a)
a.remove(9)
print(a)
