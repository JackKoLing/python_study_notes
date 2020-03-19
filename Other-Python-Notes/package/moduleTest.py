# coding : utf-8

def cal(x , y):
    m = x + y
    return m

def test():
    print("模块测试结果:" , cal(3 , 4))

# print(__name__) # 在模块中调用 name是 __main__
if __name__ == '__main__':
    test() # 所以，对于模块测试，把测试的代码放在if内判断，这样既可以自己测试，也可以给人家调用