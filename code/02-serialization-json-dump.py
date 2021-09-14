# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/9/14 13:07
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""
'''
    通过dump实现序列化
'''
import json

# dump在将对象转换为字符串的同时，指定一个文件对象，然后把转换的字符串写入到这个文件中
names = ['tom','jack','merry']
fp = open('names.txt','w')
json.dump(names,fp)
fp.close()