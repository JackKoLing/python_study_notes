# coding : utf-8

""" 小测试：验证用户密码 """
password = '147258'
count = 3
while count :
    count -= 1 # 用减法更好，因为可以直接打印剩余次数。并且如果是减法，循环直接while true
    p = input("请输入密码：")
    if p == password:
        print("密码输入成功")
        break
    elif count == 0:
        print('密码错误，不允许进入')
    else:        
        print('密码错误，你还有', count , '次机会')

""" 小测试：模拟pow(x,y),表示x的y次方"""
def power(x , y):
    res = 1
    while y:
        y -= 1
        res *= x
    return res
x = int(input('请输入x:'))
y = int(input('请输入y:'))
print('他们的pow为：', power(x , y))

""" 小测试：统计一个子串在主串中出现的次数 """
a = input("请输入主字符串：")
b = input('请输入子串：')
n = a.count(b) # 统计子串b在主串a中出现的次数
print('子串出现次数为：' , n)

""" 学习切片,list[起始：结束：步长],其中切片顾头不顾尾，步长默认为1 """
a = [2 , 4 , 5 , 3 , 7]
print(a[:]) #全切，等于复制,[::]也是复制
print(a[0:2]) #取0、1,步长默认为1
print(a[0::2]) #取0到最后，步长为2，可写成[::2]
print(a[::-1]) # 步长为-1,表示元素从后往前输出

""" 小测试：列表训练 """
list1 = ['hello' , 'seven' , ['yr' , ['h' , 'mike'] , 'all'] , 123 , 456]
list2 = list1[:] 
print(list2[2][1][0]) # 读取列表内的嵌套元素
list1[2][1][1] = 'lucy'
print(list1)

""" 小测试：做一个通讯录 """
phone = {'jackko':136022 , 'anney':123323 , 'kobe':435333 ,'james':2332421}
print('---欢迎进入通讯录---')
print('---1、查找联系人----')
print('---2、退出通讯录----')
while True:
    try:
        num = int(input('请输入指令数字：'))
        if num == 1:
            name = input('请输入联系人姓名：')
            if name in phone:
                print(name, ":" , phone.pop(name))
            else:
                print('该联系人不存在')
        elif num != 2:
            print('输入指令数字有误')
        else:
            print('感谢使用通讯录！')
            break
    except ValueError as reason:
        print('输入有误')

""" 小测试：文件练习 """
filename = input('请输入文件名：')
context = input('请输入文件内容：')
filename = 'cxy\\' + filename
f = open(filename , 'w')
f.write(context)
f.close() #总是忘记关闭文件            
