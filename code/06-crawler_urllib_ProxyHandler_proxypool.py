# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/9/17 21:59
# @Author   :endless
# @Email    :endliss@sina.cn
------------------------------
"""
'''
    创建代理池爬取数据
'''
import ssl,urllib.request,random

url = 'http://www.baidu.com/s?wd=ip'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
}
proxies_pool = [
    {'http':'58.243.29.180:4570'},
    {'http':'27.44.215.155:4513'},
    {'http':'58.243.29.58:4554'},
    {'http':'58.243.29.148:4570'},
]
request = urllib.request.Request(url=url,headers=headers)
handler = urllib.request.ProxyHandler(proxies=random.choice(proxies_pool))
opener = urllib.request.build_opener(handler)
response = opener.open(request)
content = response.read().decode('utf-8')
with open('ip_proxypool.html','w',encoding='utf-8') as f:
    f.write(content)
