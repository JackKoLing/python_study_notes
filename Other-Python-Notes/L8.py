# coding : utf-8
'''
计算0-9相加的和
'''
sum = 0
for i in range(0,10):
    sum += i
print(sum) 

'''
计算1-10相乘的积
'''
mul = 1
for i in range(1,11):
    mul *= i
print(mul)

'''
交换两个变量值,引入t变量
'''
a = 1 
b = 2
t = a
a = b
b = t
print(a)
print(b)

'''
两个数排序,if条件判断可以不写括号
'''
a = 6
b = 2
if a > b :
    t = a; a = b; b = t
print(a);print(b)

'''
找出1-100之间的所有偶数
'''
for i in range(1,101):
    if i % 2 == 0:
        print(i)