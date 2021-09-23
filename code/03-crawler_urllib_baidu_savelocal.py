# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/9/14 21:19
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""
'''
    将爬取到百度首页保存到本地
'''
import urllib.request

url = 'http://www.baidu.com'
response = urllib.request.urlopen(url)
content = response.read().decode('utf-8')
fp = open('百度首页.html','w',encoding='utf-8')
fp.write(content)
fp.close()
