# coding : utf-8

""" 字符串的方法 """
# print(dir(str))
str1 = 'I love python.'
print(str1[:6]) # 切片，注意空格也是一位字符

str2 = 'i LOVE python.'
print(str2.capitalize()) # 将字符串的首字母改为大写,其余字母全部改为小写

str3 = 'I Love PyThon.'
print(str3.casefold()) # 将字符串全部改为小写

str4 = 'jaCKK KOOn btara'
print(str4.title()) # 将每个单词的第一个字符变为大写，其他写成小写

str5 = 'I love python.'
print(str5.find('o')) # 从左边开始，找出子串是否在主字符串中，若找到一个在，则返回第一个字符的索引。若不存在，则返回-1
print(str5.rfind('o')) # 从右边开始找
print(str5.find('th'))
print(str5.find('k'))

str6 = 'love'
print(str6.join('123')) # 将字符串加到子串的两个字符之间，所以不会放在最前面和最后面

str7 = '    love   '
print(str7.lstrip()) # 将字符串的左边空格全部去掉
print(str7.rstrip()) # 将字符串的右边空格全部去掉

str8 = 'I love python.'
print(str8.split()) # 不带参数，以空格为间隔切分字符串
print(str8.split('o')) # 以o为间隔，切分字符串

str9 = ' I love python.'
print(str9.translate(str.maketrans('o' , 'k'))) # 将字符串中的所有o换成k


""" 学习字符串的格式化 """
print('{0} love {1}.'.format('I' , 'python')) # 0、1是位置参数，可以换成关键字参数
print('{a} love {b}.'.format(a = 'I' , b = 'python'))
'''
格式化操作符%
%s 格式化字符串 
%d 格式化整数
%f 格式化浮点数
%c 格式化字符及其ASCII码
%o 格式化八进制整数
%x 格式化十六进制整数
%e 科学计数法格式化浮点数
%g 根据值的大小决定使用%f或者%e
'''
print('%s'%'I love python') # 形式为：'%s' % '替换的内容'
print('%s love %s'%('I' , 'python'))
print('I am %d years old now.'%20)
print('%d + %d = %d'%(2 , 3 , 5))
print('%f'%1.232) # 默认精确到6位小数，不够用0补充
print('%.1f'%1.232) # 规定小数点后只有一位
print('%5.1f'%1.232) # 规定总宽度为5，不够用空格补充
print('%05.2f'%1.232) # 总宽度为5（其中小数点占1位），不够用0填充，小数保留2位
print('%05d'%3)  # 总宽度为5，不够用0补充
print('%+05d'%3) # 总宽度为5，不够用0补充，而第一位用+
print('%5d'%3) # 总宽度为5，不够用空格补充
print('%-5d'%3) # 左对齐，3在最左边，总宽度是5
print('%-05d'%3) #总宽度是5，左对齐


""" 学习正则表达式(regular expression) """
import re
# search函数中，第一个参数是pattern,即正则表达式，第二个参数是匹配的字符串
m = re.search('[0-9]' , 'abc3def') # 匹配0到9的数字，返回匹配的对象。若没找到匹配的字符，就返回None
print(m.group()) # 输出匹配的字符
b = re.search('\d' , 'abc3def') # \d等同于[0-9],也是匹配一个数字
print(b.group()) 
c = re.search('00\w' , 'text005.txt') # \w可以匹配一个数字或字母
print(c.group())
d = re.search('n.' , 'python!') # .可以匹配除换行符\n外的任何单字符，即数字、字母、符号等等
print(d.group())
e = re.search('\d{3}' , '032423') # {n}表示匹配n个
print(e.group())
f = re.search('\d{1,4}' , '032423') # {n,m}表示匹配n到m个，优先匹配m个，如果没有，就匹配m-1个，至少n个，注意{}不能有空格
print(f.group())
g = re.search('\d\s\w' , '011 ae2') # \s表示可以匹配任何空白字符，包含空格、换行符等
print(g.group())
h = re.search('\s+' , '21 22') # +表示至少一个字符，把符合的都匹配出来
print(h.group())
i = re.search('a?b' , 'b') # ?表示匹配一个字符或没匹配
print(i.group())
j = re.search('[0-9a-zA-Z]' , 'b_3_afi') # [0-9a-zA-Z]可以匹配一个数字或字母
print(j.group())
k = re.search('[0-9a-zA-Z]+' , '！_a3fi') # [0-9a-zA-Z]+ 表示可以匹配至少一个数字或字母，把符合的都匹配出来
print(k.group())
l = re.search('(P|p)ython','Python') # (A|B)可以匹配A或B
print(l.group())
m = re.search('(P|p)ython','python')
print(m.group())
n = re.search('^\d' , '4rq4i2') # ^表示一行的开头，^\d表示匹配开头的数字
print(n.group())
o = re.search('\d$' , '4rq4i2') # $表示一行的结尾，\d$表示匹配结尾的数字
print(o.group())
p = re.search('^python$' , 'python') # ^python$ 表示匹配整行, ^py$表示整行是p开头y结尾
print(p.group())

print(re.match('[a-z]+' , 'python')) # match要求从第一个字符就开始匹配，成功则返回对象
print(re.match('[a-z]+' , '123python')) # 不成功则是None
q = re.search('[a-z]+' , '123python') # search是从字符串中找符合的第一个位置，span=(3,9)表示位置是3-8
print(q.start()) # 返回匹配的开始位置
print(q.end()) # 返回匹配结束位置
print(q.span()) # 返回一个元组表示匹配位置
r = re.findall('\d' , '我有1个苹果、2个梨子和5个桃子。') # findall返回所有匹配结果，组成字符串列表.注意不是对象，所以不能r.group()
print(r)