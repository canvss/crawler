# -*- coding: utf-8 -*-
# @Time    : 2021/9/27 21:51
# @Author  : endless
# @FileName: 09-crawler_bs4_starbucks_menu.py
# @GitHub  ：https://github.com/epover

import urllib.request,json
from bs4 import BeautifulSoup

url = 'https://www.starbucks.com.cn/menu/'
response = urllib.request.urlopen(url=url)
content = response.read().decode('utf-8')

soup = BeautifulSoup(content,'lxml')
menu_list = soup.select('ul[class="grid padded-3 product"] strong')

for menu in menu_list:
    print(menu.get_text())