# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/9/16 22:02
# @Author   :endless
# @Email    :endliss@sina.cn
------------------------------
"""
'''
    利用cookie爬取登录后的页面
'''

import urllib.request,ssl

def create_request():
    url = 'https://www.gulixueyuan.com/'
    headers = {
        'Cookie':'UM_distinctid=17937a0167455d-093b0867be2721-113a6054-13c680-17937a01675fdc; CNZZDATA1264603569=531034137-1620133818-null%7C1631791587; online-uuid=DCDFF27A-CFB5-2B26-5BB9-82FB28A78807; PHPSESSID=ftss7rtoujh5fevl4ccg8kpf57; REMEMBERME=Qml6XFVzZXJcQ3VycmVudFVzZXI6ZFhObGNsOW5ZVzlyT1RFeE1HUkFaV1IxYzI5b2J5NXVaWFE9OjE2NjMzMzY4MzY6MDIyNjUyMTYwZDRhZmM4Yzg3NTY1NjdlZmU4MDYyMTk1MmUwMzRmZTQ1ZDdkY2MyYWJlZmI3OTE5OGZlZGU5MA%3D%3D',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        'Referer': 'https://www.gulixueyuan.com/login'
    }
    return urllib.request.Request(url=url,headers=headers)

def get_content(request):
    return urllib.request.urlopen(request,context=ssl.SSLContext()).read().decode('utf-8')

def download(content):
    with open('sgg.html','w') as f:
        f.write(content)

if __name__ == '__main__':
    request = create_request()
    content = get_content(request)
    download(content)