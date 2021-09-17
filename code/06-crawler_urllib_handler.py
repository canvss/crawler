# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/9/17 20:37
# @Author   :endless
# @Email    :endliss@sina.cn
------------------------------
"""
import ssl,urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def request():
    url = 'http://www.baidu.com'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    }
    return urllib.request.Request(url=url,headers=headers)

def HTTPHandler():
    return urllib.request.HTTPHandler()

def opener(handler):
    return urllib.request.build_opener(handler)

def save_page(content):
    with open('baidu.html','w') as f:
        f.write(content)


if __name__ == '__main__':
    response = opener(HTTPHandler()).open(request())
    save_page(response.read().decode('utf-8'))