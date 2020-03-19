# coding: utf-8

""" 第4章：操作列表 """

# 4.1 遍历整个列表
magicians = ['alice' , 'david' , 'carolina']
for magician in magicians:
    print(magician.title() + ",that was a great trick!")
    print("I can't wait to see your next trick," + magician.title() + '.\n')
print("Thank you,everyone.That was a great magic show!")

# 4.3 创建数值列表
for value in range(1,5):
    print(value) # range()是顾头不顾尾

numbers = list(range(1,6)) # 默认步长为 1
print(numbers)

even_numbers = list(range(2,11,2)) # 指定步长为2
print(even_numbers)

# 将前十个整数的平方加入列表
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

# 列表解析：将for循环和创建新元素的代码合并为一行，并自动附加新元素
squares = [value**2 for value in range(1,11)] 
# 先定义表达式来生成列表元素，再写for循环
print(squares)

#  对数字列表进行简单的统计
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# 4.4 切片，使用列表的一部分
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:3]) # 指定开始索引和结束索引+1，也是顾首不顾尾
print(players[:3]) # 没有指定第一个索引，默认从列表开头开始
print(players[2:]) # 没有指定第二个索引，默认到列表末尾
print(players[-3:]) # 输出倒数三个元素

# 遍历切片
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# 复制切片
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # 使用切片复制
# friend_foods = my_foods # 直接复制行不通，最终指向的是同一个列表
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# 4.5 元组：元素类型可不一样，值不可修改，
# 列表元素类型可不一样，值可修改。因为python不管数据类型
dimensions = (200, 50) # 元组用于存储不变的数据,若要修改数值，可以直接重新赋值变量
print(dimensions[0])
print(dimensions[1])
for dimension in dimensions:
    print(dimension)