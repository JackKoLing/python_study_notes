# coding: utf-8

""" 对象=属性+方法，把对象放一起形成一类，python是面向对象的语言，一切皆对象"""
class Student:
    'this class is a student' # 使用一串字符串来描述该类，注意不用注释
    age = 13
    def __init__(self, name): # 特殊的方法：初始化，左右有两个下划线，创建对象时自动调用此方法
        self.name = name # self是代指新建的该对象
        print(self.name)
    def show(self):
        print(self.age)
p1 = Student('Jackko') # 创建对象
p2 = Student("Anney") # 修改对象的属性
p1.name = "kobe"
print(p1.name)
del p1.name # 删除该对象的 name 属性,不能删除age
# del Student.age # age是共有属性，删除用Student.age
print(hasattr(p1 , 'name')) # 判断该对象是否有此属性
print(getattr(p1 , 'age')) # 获取该对象的该属性
setattr(p2 , 'name' , 'Bryant') # 修改该对象的属性,可以直接赋值
print(p2.name)
delattr(p2 , 'name') # 删除该对象的属性，可以直接 del p2.name,但不能直接删除age,因为age是共有的属性
print(hasattr(p2 , 'age'))
print(Student.__doc__) # 获取该类的描述信息
print(Student.__name__) # 获取类名
print(Student.__bases__) # 获取父类的构成元素 

""" 学习父类子类继承,父类包含所有子类的共同点，即子类继承父类的所有属性和方法 """
class Parent(object):  # 参数出现object，说明没有父类了
    def p(self):
        print("正在调用父类的方法")
class Child(Parent):
    def c(self):
        print("正在调用子类的方法")
    def p(self): # 子类出现和父类相同的属性或方法，直接覆盖掉父类的,所以子类要想改父类的方法，直接重命名
        print("oh no")
p1 = Child()
p1.p()
p2 = Parent()
p2.p()

class Animal(object):
    pass
class Dog(Animal):
    def __init__(self , name):
        self.name = name
        print(self.name)
d1 = Dog("吉娃娃")
d2 = Dog("哈士奇")
d3 = Dog("泰迪")

class Animal(object):
    pass
class Fish(Animal):
    def __init__(self , name):
        self.name = name
        print(self.name)
f1 = Fish("金鱼")
f2 = Fish("鲨鱼")
f3 = Fish("鲤鱼")
