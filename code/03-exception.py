# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/9/14 19:49
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""
'''
    异常处理
'''
try:
    fp = open('test.txt','r')
    data = fp.read()
    print(data)
    fp.close()
except FileNotFoundError:
    print('this is exception !!!')