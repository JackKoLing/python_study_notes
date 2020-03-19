# coding: utf-8
'''
求列表元素累加、求平均数
'''
sum = 0
nums = [78 , 91 , 20 , 37]
l = len(nums)
for num in nums:
    sum = sum + num
ave = sum / l
print(sum)
print(ave)

s = 0
nums = list(range(1,51))
for i in nums:
    s = s + i
print(s)
print(s / len(nums))

sum = 0
l = list(range(2,84))
for i in l:
    sum = sum + i
print(sum / len(l))

'''
求元素累乘
'''
a = 1
nums = [2 , 3, 4, 5, 6]
for num in nums:
    a = a * num
print(a)

a = 1
nums = list(range(9,11))
for num in nums:
    a = a * num
print(a)

'''
统计列表中某个元素出现次数、求该元素出现概率
'''
count = 0
snacks = ["chips" , "chocolate" , "cookie" , "chocolate" , "banana"]
for snack in snacks:
    if snack == "chocolate":
        count = count +1
print(count)

l = len(snacks)
ratio = float(count / l)
print(ratio)

count = 0
list = [4 , 1 , 2 , 3 , 1 , 6 , 1 , 4]
for i in list:
    if i == 1:
        count += 1 
print(count / len(list))