# coding : utf-8
""" 学习元组tuple、访问 """
tuples = ('x' , 'y' , 'z') # 也可以写成 tuples = 'x' , 'y' , 'z'  括号或没有括号的是元组，[]是列表
print(tuples)
print(type(tuples))

tuples1 = () # 空元组
tuples2 = (123) # 这个是整数类型
tuples3 = (123 , ) # 这个才是元组，一个元素的元组必须加逗号,但是一个元素的列表不用逗号
print(type(tuples3))

print(tuples[1]) # 访问和列表是一样的，用 [i]
# tuples[1] = 'k' # 元组元素不能修改,不能删除，但是可以删除整个元组，或者拼接
del tuples3 # 删除整个元组

""" 元组拼接 """
tuples1 = ('apple' , 'banana' , 'orange')
tuples2 = ('1' , '2' , '3')
tuples3 = tuples1 + tuples2
print(tuples3)
print(len(tuples3))

tuples4 = (1 , ) * 4
print(tuples4)

""" 元组遍历 """
tup1 = ("hello" , "apple" , 0 , 1)
for i in tup1:
    print(i)

""" 学习字典 dictionary """
dic = {'name':'jackko' , 'city':'Guangzhou'} # {key : value},注意key是唯一，只能用字符串、数字、元组，不能用列表
print(type(dic))
print(dic['city']) # 访问元素依然是用[]，但是不是数字，因为没有顺序，而是用键来找元素,同样的键会覆盖

""" 增加、修改、删除元素 """
dic['age'] = 15
print(dic)
dic['age'] = 25
print(dic)
del dic['age']
print(dic)
dic.clear() # 清除整个字典，但是还存在
print(dic)
del dic # 直接删除字典，字典不存在
# print(dic)

""" 字典遍历 """
# 遍历 key
d = {'list': [1 , 2 , 3], 'apple': '苹果', 'tup': (4 , 5 , 6) , 1: 789}
for key in d:
    print(key)
print(d.keys()) # 将字典的所有 key 列出来

# 遍历 value
for v in d.values():
    print(v)
print(d.values()) # 将字典的所有 value 列出来

# 遍历 item
for i in d.items():
    print(i)
print(d.items()) # 将字典的所有 item 列出来 ，(key , value)为一项

for key,value in d.items():
    print(key , value)

""" 创建字典 """
dic={}
dic = dic.fromkeys((1,2,3)) # 若不分配value,则默认为None
print(dic)
dic = dic.fromkeys((1,2,3) , 'number') 
print(dic)
dic = dic.fromkeys((1,2,3) , ('one' , 'two' , 'three')) # 第二个参数是分配给每个key的
print(dic)

""" 判断key是否在字典中 """
d = {}
d = d.fromkeys(range(5) , 'num')
print(d)
print(2 in d) # 注意是key,不是value
print(6 in d)

""" 弹出字典的值 """
a = {1:'one' , 2:'two' , 3:'three'}
a.pop(2) # 按key弹出
print(a)
print(a.popitem()) # 随机弹出任意项（key , value）
print(a)

""" 更新字典 """
c = {1:'one'}
print(c)
e = {1:'two' , 2:'two'}
c.update(e) # 若相同的 key，则更新，若不同 key ,则添加
print(c)