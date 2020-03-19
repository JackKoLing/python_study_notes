# coding: utf-8

""" 第5章：if语句 """

# 5.1 示例
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# 检查特定值是否包含着列表中
print("audi" in cars)
print("audi" not in cars)

# 5.2 条件测试
requested_topping = 'mushrooms'
if requested_topping != 'anchovices':
    print("Hold the anchovies!")

# 5.3 if语句
# if-else语句
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry,you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# if-elif-else结构
age = 17
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65: 
    # 最后还是用elif可以去除很多乱七八糟输入
    price = 5
print("Your admission cost is $" + str(price) + ".")

# 5.4 确定列表不是空,这种手法常用于循环前判断
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")