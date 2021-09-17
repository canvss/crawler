# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/9/17 21:15
# @Author   :endless
# @Email    :endliss@sina.cn
------------------------------
"""
'''
 通过ProxyHandler代理ip爬取数据
'''

import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def request():
    url = 'http://www.baidu.com/s?wd=ip'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    }
    return urllib.request.Request(url=url,headers=headers)

def ProxyHandler():
    proxies = {
        'http':'117.69.230.204:3256',
    }
    return urllib.request.ProxyHandler(proxies=proxies)

def save_page(content):
    with open('ip_proxy.html','w',encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    opener = urllib.request.build_opener(ProxyHandler())
    response = opener.open(request())
    save_page(response.read().decode('utf-8'))