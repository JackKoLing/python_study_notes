# coding : utf-8

""" 单异常处理 """
try:
    f = open('cxy\\file.txt') # 不写模式，就是默认只读 r
    print(f.read())
    f.closed()
except FileNotFoundError as reason:
    print("文件读取失败\n失败原因是" + str(reason))

try:
    num1 = input('请输入被除数：')
    num2 = input('请输入除数：')
    res = int(num1) / int(num2)
    print('除法结果是：' , res)
except ZeroDivisionError:
    print('0不能做除数')

""" 多异常处理 """
# 这里第一句就有异常，所以直接跳到TypeError,try后面语句不会执行
try:
    sum = 1 + '1'
    f = open('cxy\\file.txt')
    print(f.read())
    f.close()
except FileNotFoundError as reason:
    print('出错了。\n原因是：' + str(reason))
except TypeError as reason:
    print('出错了。\n原因是：' + str(reason))

# 也可以将其放在一起，若都没有捕捉到异常，那就程序停止了
try:
    int('abs')
    sum = 1 + '1'
    f = open('cxy\\file.txt')
    print(f.read())
    f.close()
except (FileNotFoundError, TypeError) as reason:
    print('出错了。\n原因是：' + str(reason))

finally是无论有没有异常都会执行
try:
    f = open('cxy\\file.txt' , 'w')
    f.write("hi")
    # sum = 1 + '1'
    # f.close()  # python2不能放这里，因为不能保存，但是python3可以
except (OSError, TypeError) as reason:
    print('出错了。\n原因是：' + str(reason))
finally:
    f.close()

""" 异常中else使用 """
try:
    int('123')
except ValueError as reason:
    print('出错了')
else: 
    print('没有异常发生')
