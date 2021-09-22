# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/9/15 22:19
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""
'''
    使用请求定制对象发起post请求获取百度翻译数据
'''

import urllib.request
import urllib.parse
import ssl,json

def get_post_baidu_translate():
    url = 'https://fanyi.baidu.com/sug'
    data = {
        'kw': 'crawler'

    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    }
    # post请求参数必须进行编码
    new_data = urllib.parse.urlencode(data).encode('utf-8')
    # post请求参数需要放在请求定制对象中
    request = urllib.request.Request(url=url,data=new_data,headers=headers)
    response = urllib.request.urlopen(request,context=ssl.SSLContext())
    content = response.read().decode('utf-8')
    # 将字符串转为json对象
    resp_obj = json.loads(content)
    print(resp_obj)

get_post_baidu_translate()