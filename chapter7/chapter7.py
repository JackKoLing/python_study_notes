# coding: utf-8

""" 第7章：用户输入和while循环 """

# 7.1 input()实例
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")

height = int(input("How tall are you, in inches? "))
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

number = int(input("Enter a number, and I'll tell you if it's even or odd: "))
if number % 2 == 0:
    print("\nThe number " + str(number) + " is enev.")
else:
    print("\nThe number " + str(number) + " is odd.")

# 7.2 while循环简介
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# 让用户选择何时退出，设立标志
promt = "\nTell me something, and I will repeat it back to you: "
promt += "\nEnter 'quit' to end the program. "
flag = True
while flag:
    message = input(promt)
    if message == 'quit':
        flag = False
    else: 
        print(message)

# 在循环中使用continue，可返回到循环开头
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# 7.3 使用while循环来处理列表和字典，可遍历的同时进行修改
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    # 若用for循环遍历，则不能同时删除列表元素
    current_user = unconfirmed_users.pop() 
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# 删除包含特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
# 法一
# for pet in pets:
#     if pet == 'cat':
#         pets.remove('cat')
# print(pets)

# 法二 使用while更快一点
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# 使用用户输入来填充字典
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat's your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response
    repeat = input("Would you like to let another person respond?(yes/no) ")
    if repeat == 'no':
        polling_active = False
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + "would like to climb " + response + ".")