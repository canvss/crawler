# -*- coding: utf-8 -*-
# @Time    : 2021/9/27 22:17
# @Author  : endless
# @FileName: 09-crawler_bs4_starbucks_menu_picture.py
# @GitHub  ：https://github.com/epover

import urllib.request,json
from bs4 import BeautifulSoup
from util import str_replace

def down_load(menu_name_list,picture_url_list):
    for i in range(len(menu_name_list)):
        file_name = './starbucks_menu_picture/'+menu_name_list[i].get_text()+'.jpg'
        picture_url = 'https://www.starbucks.com.cn'+menu_picture_list[i].get('style').split('"')[1].split('"')[0]
        try:
            urllib.request.urlretrieve(picture_url,file_name)
        except FileNotFoundError:
            name = menu_name_list[i].get_text().replace('/',' ')
            file_name = './starbucks_menu_picture/'+name+'.jpg'
            urllib.request.urlretrieve(picture_url, file_name)

    print('over')


if __name__ == '__main__':
    url = 'https://www.starbucks.com.cn/menu/'
    response = urllib.request.urlopen(url=url)
    content = response.read().decode('utf-8')

    soup = BeautifulSoup(content, 'lxml')
    menu_name_list = soup.select('ul[class="grid padded-3 product"] strong')
    menu_picture_list = soup.select('div[class="preview circle"]')
    down_load(menu_name_list,menu_picture_list)