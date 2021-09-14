# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/9/13 13:51
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""
'''
    dumps实现序列化
'''

import json

file = open('names.txt','w')
names = ['tom','jack','marry']
# 通过json.dumps将python对象转换成json字符串
result = json.dumps(names)
print(type(result))
# 将json字符串写入文件
file.write(result)
file.close()