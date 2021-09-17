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
        'Referer': 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=ip%E6%9F%A5%E8%AF%A2&oq=ip%25E6%259F%25A5%25E8%25AF%25A2&rsv_pq=93fa920200008ca9&rsv_t=e38bd2devLnU2pnYyuiCFdtzwh3I3gTa0RM85dJNYYIowWwE%2BMJwdn%2FecFA&rqlang=cn&rsv_dl=tb&rsv_enter=1&rsv_btype=t&inputT=5&rsv_sug3=9&rsv_sug1=3&rsv_sug7=100&rsv_sug2=0&rsv_sug4=721'
    }
    return urllib.request.Request(url=url,headers=headers)

def ProxyHandler():
    proxies = {
        'http':'27.44.215.155:4513',
    }
    return urllib.request.ProxyHandler(proxies=proxies)

def save_page(content):
    with open('ip_proxy.html','w',encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    opener = urllib.request.build_opener(ProxyHandler())
    response = opener.open(request())
    save_page(response.read().decode('utf-8'))