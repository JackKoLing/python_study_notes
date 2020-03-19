# coding : utf-8

""" 学习文件操作：获取文件对象 """
# w表示写文件，如果文件存在，则原内容会删除，从头开始写。若不存在，则创建新文件
f = open('cxy\\test.txt' , 'w') # open()返回的是文件对象
print('文件名称：' , f.name)
print("文件是否关闭：" , f.closed)
print('文件访问模式：', f.mode)
f.close() # 关闭文件
print("文件是否关闭：" , f.closed)

# f = open('cxy\\test.txt' , 'r') # r表示只能读，不能写
f = open(r'cxy\test.txt' , 'r') # 路径可以用双\\，或者单/，或者使用单\，但是要在路径前加 r 来反转义
print(f.name)

""" 读取文件内容 """
f = open("cxy\\test.txt" , 'r') # f是文件对象
s = f.read() # 读文件
print('文件的内容是：\n' , s)

""" 往文件中写内容 """
f = open("cxy\\test1.txt" , 'w')
f.write("I am learning python.\nI love python.")
f.close() # 写完内容后记得关闭文件，文件才会保存下来

""" 文件操作 """
import os
os.rename("cxy\\test1.txt" , "cxy\\test2.txt") # 修改文件名
os.remove("cxy\\test2.txt") # 删除文件
