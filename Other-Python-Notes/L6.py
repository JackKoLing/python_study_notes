# coding: utf-8
'''
学习循环语句:
for num in nums:
for value in range(1,5):  # 注意不包括5,故range(1,5)是1、2、3、4
for i in range(5): # 输出5遍，因为默认从0开始，即0、1、2、3、4
'''
nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)

color = ["red" , "yellow" , "green"]
for c in color:
    print(c)
print("I like them all.")

for value in range(1,5):
    print(value)

for n in range(3,6):
    print(n)

a = list(range(1,5))
b = list(range(5)) # 默认从0开始
c = list(range(2,10,3)) # 以3个数为间隔 2、2+3、2+3+3
print(a)
print(b)
print(c)

for n in range(3,6):
    print("hello. ")

for i in range(3):
    print("i love u.")