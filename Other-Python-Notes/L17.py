# coding : utf-8

""" 小测试：获取输入名字 """
name = input("请输入你的名字：")
print("你好，" + name)

""" 小测试： 输入1~100的数字"""
num = int(input("请输入1~100的数字:"))
if 1 <= num <= 100 : 
    # num >=1 and num <= 100不用这么麻烦，可以直接拼接
    print('在范围内') 
else:
    print('不在范围内')

""" 小测试：找出1-10的奇数 """
# 法一
i = 1
while i <= 10:
    print(i)
    i += 2

# 法二
for i in range(1 , 11):
    if i % 2 != 0:
        print(i)

""" 小测试：判断年份是否闰年 """
year = int(input("请输入年份："))
if ((year % 4 ==0 and year % 100 != 0) or (year % 400 == 0)):
    print('该年份是闰年')
else:
    print('该年份不是闰年')

""" 小测试：输入成绩，给出成绩级别 """
score = int(input('请输入分数：'))
if score < 0 or score > 100:
    print('分数输入错误')
elif 90 <= score <= 100:
    print('该分数为A')
elif 70 <= score < 90:
    print('该分数为B')
elif 60 <= score < 70:
    print('该分数为C')
else:
    print('该分数为D')

""" 
小测试：12个球，其中3红3白6黑，任取8个有几种搭配 
实质是黑球取2-6个，红球取0-3个，白球取0-3个
"""
count = 0
for red in range(0 , 4):
    for white in range(0 , 4):
        for black in range(2 , 7):
            if red + white + black == 8:
                print("红、白、黑各为：" , red , white , black)
                count += 1
print('共有' + str(count) + '种方案')
# print('共有',count,'种方案')

