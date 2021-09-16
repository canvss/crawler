# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/9/16 20:36
# @Author   :endless
# @Email    :endliss@sina.cn
------------------------------
"""
'''
    爬虫中常见HTTPError,URlError异常
'''

import urllib.request,ssl,urllib.error

def get_cnsd_article():
    url = 'https://blosdas.csdn.net/sugar_no1/article/details/883179501'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    }
    request = urllib.request.Request(url=url,headers=headers)
    return urllib.request.urlopen(request,context=ssl.SSLContext())

if __name__ == '__main__':
    try:
        response = get_cnsd_article()
        content =response.read().decode('utf-8')
        print(content)
    except urllib.error.HTTPError:
        print('HTTPError!!!')
    except urllib.error.URLError:
        print('please check up url !')