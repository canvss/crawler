# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/9/14 22:44
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""
'''
    使用quote对参数进行unicode转码 
'''
import urllib.request
import urllib.parse
import ssl

url = 'https://www.baidu.com/s?wd='
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
request_parameters ='张学友'
new_url = url+urllib.parse.quote(request_parameters)
request = urllib.request.Request(url=new_url,headers=headers)
response = urllib.request.urlopen(request,context=ssl.SSLContext())
content = response.read().decode('utf-8')
print(content)