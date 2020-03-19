# coding: utf-8

""" 第3章：列表简介 """
 
# 3.1 查询（读取）列表
bicycles = ['trek' , 'cannondale' , 'redline' , 'specialized']
print(bicycles)
print(bicycles[0].title())
print(bicycles[-1]) # 返回最后一个元素，适用于不知道元素个数的情况
print(bicycles[-2]) # 返回倒数第二个元素

message = "My first bicycle was a " + bicycles[1].title() + "."
print(message)

# 3.2 修改、增加、删除列表元素
motorcycles = ['honda' , 'yamaha' , 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati' # 修改指定的元素
print(motorcycles)

motorcycles.append('honda') # 在列表末尾添加元素
print(motorcycles) 

motorcycles.insert(1 , 'newcar') # 可以指定某个位置插入元素
print(motorcycles)

del motorcycles[1] # 使用del删除指定的元素,不需要引用删除的元素
print(motorcycles)

poped_motorcycle = motorcycles.pop() # 使用pop()删除元素，适用于需要引用刚删除的元素
print(motorcycles)
print('The last motorcycle I owned was a ' + poped_motorcycle.title() + '.') # 若不设置参数，则弹出最后一个元素

first_owned = motorcycles.pop(0)
print(motorcycles)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

too_expensive = 'suzuki'
motorcycles.remove(too_expensive) # 使用remove()删除元素，适用于只知道元素的名称，不知道索引的情况
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")


# 3.3 组织列表
cars = ['bmw' , 'audi' , 'toyota' , 'subaru']
cars.sort() # 使用sort（）按字母顺序进行永久性排序
print(cars)
cars = ['bmw' , 'audi' , 'toyota' , 'subaru']
cars.sort(reverse=True)
print(cars) # 按字母反序进行永久性排序
cars = ['bmw' , 'audi' , 'toyota' , 'subaru']
print(sorted(cars)) # 使用sorted()对列表按字母顺序临时排序，不改变原来列表的顺序
print(sorted(cars , reverse=True)) # 使用sorted()对列表按字母反序临时排序，不改变原来列表的顺序
print(cars)

cars.reverse()
print(cars) # 将列表倒着打印出来，永久性改变，注意不是按字母顺序
cars.reverse()
print(cars) # 两次reverse()便可恢复原来顺序

print(len(cars)) # 获取列表长度