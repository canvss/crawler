# -*- coding: utf-8 -*-
# @Time    : 2021/9/29 20:00
# @Author  : endless
# @FileName: 10-crawler_selenium_interactive.py
# @Email   : endliss@sina.cn

'''
    通过selenuim交互
'''

from selenium import webdriver
import time

path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

browser.get('https://www.baidu.com/')

# 向文本框输入内容
browser.find_element_by_id('kw').send_keys('张学友')

time.sleep(2)

# 点击百度一下
browser.find_element_by_id('su').click()

time.sleep(3)
# 滑到底部
js_bottom = 'document.documentElement.scrollTop=100000'
browser.execute_script(js_bottom)

time.sleep(3)
# 点击下一页
next = browser.find_element_by_xpath('//a[@class="n"]')
next.click()
time.sleep(2)
# 后退
browser.back()

# 前进
time.sleep(2)
browser.forward()

time.sleep(5)
# 关闭浏览器
browser.quit()