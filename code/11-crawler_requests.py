# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/5/5 21:05

import requests

url = 'https://www.baidu.com/'

response = requests.get(url=url)
response.encoding = 'utf-8'
print(response.text)
print(response.status_code)
print(response.headers)