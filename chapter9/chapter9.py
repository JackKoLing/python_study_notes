# coding: utf-8

""" 第9章：类 """

# 9.1 创建和使用类
class Dog():
    """ 一次模拟小狗的简单尝试 """

    def __init__(self, name, age):
        """ 初始化属性name和age """
        self.name = name
        self.age = age
    
    def sit(self):
        """ 模拟小狗蹲下 """
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """ 模拟小狗打滚 """
        print(self.name.title() + " rolled over!")
    
# 根据类创建实例
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()

# 9.2 使用类和实例
class Car():
    """ 一次模拟汽车的简单尝试 """

    def __init__(self, make, model, year):
        """ 初始化描述汽车的属性 """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # 里程表读数,给该属性指定默认值

    def get_descriptive_name(self):
        """ 返回整洁的描述性信息 """
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """ 打印一条指出汽车里程的消息 """
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """ 
        将里程表读数设置为指定的值 
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """ 将里程表读数增加指定值 """
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")

my_new_car = Car('audi', 'a4', 2020)
print(my_new_car.get_descriptive_name())

# 通过实例直接修改属性值
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 通过方法修改属性值,更有灵活性
my_new_car.update_odometer(20)
my_new_car.read_odometer()

# 通过方法对属性的值进行递增
my_new_car.update_odometer(23500)
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()

# 将实例用作属性，抽出类的一部分作为独立类
class Battery():
    """ 一次模拟电动汽车电瓶的简单尝试 """

    def __init__(self, battery_size = 70):
        """ 初始化电瓶的属性 """
        self.battery_size = battery_size

    def describe_battery(self):
        """ 打印一条描述电瓶车容量的消息 """
        print("This car has a " + str(self.battery_size) + "-KWh battery.")

    def get_range(self):
        """ 打印一条消息，指出电瓶的续航里程 """
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

# 9.3 继承：子类可以继承父类的所有属性和方法，还可以定义自己特有的属性和方法
class ElectricCar(Car):
    """ 电动汽车的独特之处 """
    
    def __init__(self, make, model, year):
        """
        初始化父类的属性,再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery = Battery() # 将实例用作属性    

my_tesla = ElectricCar('tesla', 'model s', 2020)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# 9.4 导入类
from car import Car, ElectricCar

my_new_car = Car('audi', 'a4', 2020)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_tesla = ElectricCar('tesla', 'model s', 2020)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# 9.5 python标准库
from collections import OrderedDict

favorite_languages = OrderedDict() # 创建一个空的有顺序的字典
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edwawrd'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

