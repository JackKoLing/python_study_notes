# coding : utf-8
'''
while循环结构
'''
a = 10
while a >= 1:
    print(a)
    a -= 2

""" 学习布尔变量True、False """
a = 10
print(a > 0)

list = ["a" , "b" , "c" , "d"]
print(len(list) == 3)

""" 退出循环break """
while(1):
    print("a")
    break
print("b")

""" while进行累加、累乘 """
sum = 0
i = 1
while(i <= 100):
    sum += i
    i += 1
print(sum)

mul = 1
i = 1
while i <= 10:
    mul *= i
    i += 1
print(mul)

""" while求列表平均数 """
list = [2 , 9 , 5]
sum = 0
i = 0
while i < len(list):
    sum += list[i]
    i += 1
print(sum / len(list))

""" while求偶数 """
a = 0
while a < 50:
    print(a)
    a +=2

