# coding: utf-8
'''
强制转换类型：int()、str()
找出列表中最大最小的元素：max()、min()
找出列表的长度：len()
求数的绝对值：abs(),因为绝对的英文是"absolute"
计算x的y次方：pow(x,y)
'''
a = 3.1415926
print(a)
b = int(a) # 直接把后面的小数去掉，不是四舍五入
print(b)

list = [1 , 2, 3, 5 , 1, 6]
print(list)
a = max(list)
b = min(list)
print(a)
print(b)

color = ["red" , "green" , "blue"]
print(color)
l = len(color)
print(l)

print(abs(-12))
print(abs(-30) + abs(-9))

x = 10
y = 2
print(pow(x,y))
print(pow(6,1))
