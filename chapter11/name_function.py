# coding: utf-8

# 11.1 测试函数

def get_formatted_name(first, last, middle=''):
    """ 生成一个标准的全名 """
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()