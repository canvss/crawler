# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/9/14 20:52
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""
'''
    response常用方法
'''

import urllib.request

url = 'http://www.baidu.com'
response = urllib.request.urlopen(url)

# 返回对象：class 'http.client.HTTPResponse'>
print(type(response))

# 获取响应状态码
status_code = response.getcode()
print(status_code)

# 获取响应头信息
headers = response.getheaders()
print(headers)

# 获取url
url = response.geturl()
print(url)

# 读取5个字节：b'<!DOC'
# content = response.read(5)
# print(content)

# 读取一行
# content = response.readline()
# print(content)

# 一行一行的读取数据
content = response.readlines()
print(content)
