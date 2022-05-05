# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/9/15 13:13
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""
'''
    使用urlencode传递字典参数进行转码
'''
import urllib.request
import urllib.parse
import ssl

def get_webpage():
    url = 'https://www.baidu.com/s?'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    }
    data = {
        'wd':'张学友',
        'sex':'男',
        'location':'中国香港'
    }
    # 通过urlencode将参数进行unicode转码拼接
    new_url = url + urllib.parse.urlencode(data)
    # 请求对象的定制
    request = urllib.request.Request(url=new_url,headers=headers)
    response = urllib.request.urlopen(request,context=ssl.SSLContext())
    if response.getcode() == 200:
        content = response.read().decode('utf-8')
        with open('baidu.html','w',encoding='utf-8') as f:
            f.write(content)
    else:
        print('Crawl failed ！')


if __name__ == '__main__':
    get_webpage()