# coding: utf-8

""" 正则表达式 """
import re

a = re.search('ca*t' , 'ct') # *表示任意个字符（包括0个），所以ca*t可以匹配ct、cat、caaat
print(a.group()) 
b = re.search('[a-z$]' , '$aiu') # []表示范围，$本来表示行的结尾，但是在[]内，就恢复自己的含义,[a-z$]表示匹配字母或￥
print(b.group()) 
print('abc\n') # \表示转义，这里\n表示换行
print('abc\\n') # \\表示不转义，所以\\n等同于\n
print(r'abc\n') # 或者在串前加上r表示反转义,即保持原串
c = re.search(r'\\s' , '\s') # 加上r，表示反转义，保持原串,注意:匹配\s是用r'\\s'，不是r'\s'
print(c.group())
d = re.search(r'\\' , r'\\') # 匹配\ 
print(d.group())

d = re.compile(r'\d+') # 匹配至少一个数字
print(d.match('abc123def')) # 默认从0位开始匹配
print(d.match('abc123def' , 3 , 8)) # 设置从3开始，7结束

e = re.compile(r'^(\d{3})-(\d{3,8})$') # 定义了两组，括号内为一组
f = e.match('025-123456') # 返回匹配对象
print(f)
print(f.group(0)) # 返回匹配成功的整个串，也可以f.group()，默认是0
print(f.group(1)) # 返回第一个分组（）匹配成功的子串
print(f.group(2)) # 返回第二个分组（）匹配成功的子串
print(f.groups()) # 返回全部分组子串，元组格式
# print(f.group(3)) # 没有第三组

g = re.compile(r'([a-zA-Z]+) ([a-zA-Z]+)') # 这里只匹配两个单词
m = g.match('hello Cheng Jackko Anney')
print(m.groups())

print('a b   c'.split(' ')) # 以空格为切片，是无法识别连续的空格
print(re.split(r'\s+' , 'a b   c')) # 使用re.split可以正常分割
print(re.split(r'[\s,]+' , 'a,b,   c'))

n = re.compile(r'(\d+)(1*)')
o = n.match('21123111111')
print(o.groups()) # 贪婪匹配，第一组匹配了所有数字，第二组就只能匹配空字符了('21123111111', '')
p = re.compile(r'(\d+?)(1*)') # 加上问号是非贪婪匹配，匹配到就好
q = p.match('21123111111')
print(q.groups()) # 非贪婪匹配，第一组匹配到就好，第二组贪婪匹配('2', '11')
r = re.compile(r'^(\d+?)(1*)$') # 加上问号是非贪婪匹配，匹配到就好,这个是整行的匹配
s = r.match('2123111111')
print(s.groups()) # 非贪婪匹配，第一组匹配到就好,不抢第二组的，第二组贪婪匹配('2123', '111111')
t = re.compile(r'(\d+?)(1*)') # 加上问号是非贪婪匹配，匹配到就好
v = t.match('2123111111')
print(v.groups()) # 非贪婪匹配，第一组匹配到就好,不抢第二组的，第二组贪婪匹配('2', '1')

""" 学习日期和时间 """
from datetime import datetime , timedelta # 从datetime模块中导入datetime类
print(datetime.now()) # 获取当前时间
print(datetime(2050,11,7,12,00)) # 获取指定时间，这只是将我的数字改为时间标准格式
print(datetime.strptime('1997-07-01 00:00:00' , '%Y-%m-%d %H:%M:%S')) # 将字符串改为日期格式
print(datetime.now().strftime('%a , %b  %d %H:%M:%S')) # 将日期转为字符串
print(datetime.now() + timedelta(days = 2 , hours = 1)) # 计算两天后又一个小时的时间