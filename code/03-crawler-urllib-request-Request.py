# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/9/14 21:40
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""

'''
    通过urllib.request.Request来传入User-Agent
'''

import urllib.request
import ssl
url = 'https://www.baidu.com'
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request,context=ssl.SSLContext())
content = response.read().decode('utf-8')
print(content)