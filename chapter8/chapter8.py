# coding: utf-8

""" 第8章：函数 """

# 8.1 定义函数
def greet_user(username):
    """ 显示简单的问候语 """
    print("Hello, " + username.title() + "!")
greet_user('jackko')

# 8.2 传递实参
# 位置实参：要求实参的顺序与形参的顺序一一对应
def describe_pet(pet_name, animal_type='dog'):
    """ 显示宠物的信息 """
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')

# 关键字实参：无需关注顺序，而是在实参中指明了对应的形参名
describe_pet(pet_name='harry', animal_type='hamster')

# 使用默认值:必须是非默认的形参放前面，默认的形参放后面，因为位置实参对应原则
describe_pet('willie')

# 8.3 返回值
# 返回简单值,并使用默认值让实参变成可选的
def get_formatted_name(first_name, last_name, middle_name=''):
    """ 返回整洁的姓名 """
    if middle_name:
        full_name = first_name + " " + middle_name + ' ' + last_name     
    else:
        full_name = first_name + " " + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('jimi', 'hendrix', 'lee')
print(musician)

# 返回字典
def build_person(first_name, last_name, age=''):
    """ 返回一个字典，其中包含有关一个人的信息 """
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix')
print(musician)
musician = build_person('jimi', 'hendrix', age=27)
print(musician)

# 8.4 传递列表
def greet_users(names):
    """ 向列表中的每位用户都发出简单的问候 """
    for name in names:
        meg = "Hello, " + name.title() + "!"
        print(meg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# 8.5 传递任意数量的实参
# 结合使用位置实参和任意数量的实参
def make_pizza(size, *toppings):
    """ 概述要制作的pizza """
    # 形参*toppings表示创建一个toppings空元组来接收其余信息
    print("\nMaking a " + str(size) + 
         "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 使用任意数量的关键字实参：适合预先不知道函数提供什么信息的情况
def build_profile(first, last, **user_info):
    """ 创建字典，其中包含我们知道的有关用户的一切 """
    # 形参**user_info表示创建一个user_info空字典来接收其余信息
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                            field='physics',
                            age=15)
print(user_profile)

# 8.6 将函数存储在模块中
# 导入整个模块，并指定别名
import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 导入特定的函数,并指定别名
from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# 导入模块中的所有函数，但不建议这样做，容易覆盖同名函数，建议以上两种
from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')