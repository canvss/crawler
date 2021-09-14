# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/9/14 21:13
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""
'''
    使用urllib.request.urlretrieve下载文件
'''

import urllib.request

url = 'http://www.baidu.com'
urllib.request.urlretrieve(url,'baidu.html')