# -*- coding: utf-8 -*-
# @Time    : 2021/9/29 21:18
# @Author  : endless
# @FileName: 10-crawler_selenium_Chrome_handless.py
# @Email   : endliss@sina.cn

'''
    Chrome-headless
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def share_browser():
    chrome_options = Options()
    chrome_options.add_argument('‐‐headless')
    chrome_options.add_argument('‐‐disable‐gpu')
    path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    chrome_options.binary_location = path
    return webdriver.Chrome(chrome_options=chrome_options)

browser = share_browser()
browser.get('https://www.baidu.com/')


