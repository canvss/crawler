# -*- coding: utf-8 -*-
# @Time    : 2021/9/23 21:01
# @Author  : endless
# @FileName: 07-crawler_xpath_baidu.py
# @GitHub  ：https://github.com/epover

'''
    通过xpath获取百度首页百度一下字符
'''

import urllib.request
from lxml import etree

def request():
    url = 'http://www.baidu.com'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        'Referer': 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=ip%E6%9F%A5%E8%AF%A2&oq=ip%25E6%259F%25A5%25E8%25AF%25A2&rsv_pq=93fa920200008ca9&rsv_t=e38bd2devLnU2pnYyuiCFdtzwh3I3gTa0RM85dJNYYIowWwE%2BMJwdn%2FecFA&rqlang=cn&rsv_dl=tb&rsv_enter=1&rsv_btype=t&inputT=5&rsv_sug3=9&rsv_sug1=3&rsv_sug7=100&rsv_sug2=0&rsv_sug4=721'
    }
    return urllib.request.Request(url=url,headers=headers)

if __name__ == '__main__':
    httphandler = urllib.request.HTTPHandler()
    opener = urllib.request.build_opener(httphandler)
    response = opener.open(request())
    content = response.read().decode('utf-8')
    tree = etree.HTML(content)
    result = tree.xpath('//input[@id="su"]/@value')[0]
    print(result)