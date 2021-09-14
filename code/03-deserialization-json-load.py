# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/9/14 13:15
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""
import json

'''
    反序列化:json.load
'''

fp = open('names.txt','r')
result = json.load(fp)
print(type(result))
fp.close()