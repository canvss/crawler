# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/9/16 13:44
# @Author   :endless
# @Email    :endliss@sina.cn
------------------------------
"""
'''
    通过ajax爬取豆瓣电影top20
'''

import urllib.request,urllib.parse,ssl

def get_ajax_doubantop20():
    url = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    }
    request = urllib.request.Request(url=url,headers=headers)
    response = urllib.request.urlopen(request,context=ssl.SSLContext())
    content = response.read().decode('utf-8')
    with open('doubantop20.json','w',encoding='utf-8') as f:
        f.write(content)

get_ajax_doubantop20()