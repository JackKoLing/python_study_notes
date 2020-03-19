# coding: utf-8

# 11.1 测试函数

""" 单元测试和测试用例 """
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """ 测试name_function.py """

    def test_first_last_name(self):
        """ 能够正确地处理像Janis Joplin这样的姓名吗？ """
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """ 能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗？ """
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main() # 让python运行文件中所有以test_开头的方法