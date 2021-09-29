# -*- coding: utf-8 -*-
# @Time    : 2021/9/29 20:25
# @Author  : endless
# @FileName: 10-crawler_selenium_jd.py
# @Email   : endliss@sina.cn

'''
    使用selenium模拟浏览器爬取京东秒杀源码
'''

from selenium import webdriver

path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
browser.get('https://www.jd.com/')
# 获取jd源码
response = browser.page_source
print(response)
browser.quit()