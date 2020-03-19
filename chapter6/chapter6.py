# coding: utf-8

""" 第6章：字典 """

# 6.1 一个简单的字典,用key访问value
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# 6.2 使用字典
# 添加key-value
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 修改value,直接赋值
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

# 删除key-value
print(alien_0)
del alien_0['points']
print(alien_0)

# 字典可以存储一个对象的多种信息
student_1 = {
    'name': 'Jackko',
    'age': 24,
    'school': 'SCAU', # 最后一个允许写逗号，为添加下一个key-value做准备
}
print(student_1)

# 字典也可以存储由类似对象组成的同一种信息
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
# 学习将较长的print语句分行
print("Sarah's favorite language is " + 
    favorite_languages['sarah'].title() + 
    ".")

# 6.3 遍历字典
# 遍历所有信息，即key-value
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + 
    language.title() + ".")

# 按顺序遍历字典中的所有键
for name in sorted(favorite_languages.keys()):
    # 默认是遍历所有的键，所以可以 for name in favorite_language:
    print(name.title())

# 使用集合，遍历字典中的所有值(去除重复)
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# 6.4 嵌套
# 字典列表：将字典嵌套在列表中
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# 列表字典：将列表作为值，嵌套在字典中
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print("\n" + name.title() + "'s favorite language is " + languages[0])
    else:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())

# 在字典中存储字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },

}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())