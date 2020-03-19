# coding: utf-8
""" 定义函数并调用 """
def greet():
    print("Nice to meet you.")
    return
greet()

def mul(a , b , c):
    return a * b * c
res = mul(2 , 3 , 4)
print(res)

def info(name , age):
    print("Name:" , name)
    print("Age:" , age)
    return
info("Anna" , 22)

def check(score):
    if score > 90:
        return "优秀"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"
print(check(30))

""" 学习局部变量、全局变量 """
def plus(a , b):
    y = a + b
    return y
res = plus(3 , 4)
print(res)