# -*- coding: utf-8 -*-
# @Time    : 2021/9/29 21:06
# @Author  : endless
# @FileName: 10-crawler_selenium_Phantomjs.py
# @Email   : endliss@sina.cn

'''
    使用Phantiomjs
    1.无界面的浏览器
    2.支持页面元素查找
    3.由于不进行css和gui渲染，运行效率高
'''

from selenium import webdriver


browser = webdriver.PhantomJS('phantomjs.exe')
browser.get('https://www.baidu.com/')
# 保存屏幕快照
browser.save_screenshot('baidu.png')
browser.find_element_by_id('kw').send_keys('刘德华')
browser.find_element_by_id('su').click()
browser.save_screenshot('刘德华.png')
browser.quit()